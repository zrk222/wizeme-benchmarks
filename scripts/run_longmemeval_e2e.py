from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from common import now_iso, read_json, write_json


SYSTEM_PROMPT = (
    "Answer the question only from the supplied conversation memory. "
    "Treat dates and speaker roles as evidence. If the memory does not support "
    "an answer, say you do not know. Keep the answer concise and factual."
)


def post_openrouter(api_key: str, model: str, prompt: str) -> tuple[str, int]:
    payload = json.dumps(
        {
            "model": model,
            "temperature": 0,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/zrk222/wizeme-benchmarks",
            "X-Title": "WizeMe LongMemEval",
        },
        method="POST",
    )
    started = time.perf_counter()
    with urllib.request.urlopen(request, timeout=180) as response:
        body = json.loads(response.read().decode("utf-8"))
    latency_ms = round((time.perf_counter() - started) * 1000)
    return str(body["choices"][0]["message"]["content"]).strip(), latency_ms


def session_text(row: dict[str, Any], session_id: str) -> str:
    try:
        index = [str(value) for value in row["haystack_session_ids"]].index(session_id)
    except ValueError:
        return ""
    date = str(row["haystack_dates"][index])
    turns = row["haystack_sessions"][index]
    lines = [f"Session {session_id} ({date})"]
    for turn in turns:
        role = str(turn.get("role", "unknown"))
        content = str(turn.get("content", "")).strip()
        if content:
            lines.append(f"{role}: {content}")
    return "\n".join(lines)


def build_prompt(row: dict[str, Any], ranked_turn_ids: list[str], max_sessions: int) -> str:
    ranked_sessions: list[str] = []
    for turn_id in ranked_turn_ids:
        session_id = turn_id.rsplit("_", 1)[0]
        if session_id not in ranked_sessions:
            ranked_sessions.append(session_id)
    contexts = [
        session_text(row, session_id)
        for session_id in ranked_sessions[:max_sessions]
    ]
    contexts = [context for context in contexts if context]
    question_date = str(row.get("question_date", "unknown"))
    return (
        f"Question date: {question_date}\n"
        f"Question: {row['question']}\n\n"
        "Conversation memory:\n"
        + ("\n\n".join(contexts) if contexts else "[No relevant memory retrieved]")
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--retrieval", required=True)
    parser.add_argument("--hypotheses", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--answer-model", required=True)
    parser.add_argument("--answer-provider", default="openrouter")
    parser.add_argument("--max-sessions", type=int, default=8)
    parser.add_argument("--query-limit", type=int, default=0)
    args = parser.parse_args()

    retrieval = read_json(args.retrieval)
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    prompt_hash = hashlib.sha256(SYSTEM_PROMPT.encode("utf-8")).hexdigest()
    if not api_key:
        write_json(
            args.result,
            {
                "schema_version": "1.0",
                "system": "WizeMe",
                "status": "not_run",
                "dataset": retrieval["dataset"],
                "evaluation": {
                    "task": "long-term-memory-qa",
                    "mode": "end_to_end_qa",
                    "granularity": "answer",
                    "metric_definition": "Official LongMemEval answer generation plus the unmodified official gpt-4o judge.",
                    "evaluator_revision": retrieval["evaluation"]["evaluator_revision"],
                },
                "metrics": {},
                "provenance": {
                    "generated_at": now_iso(),
                    "source": "scripts/run_longmemeval_e2e.py",
                    "command": "OPENROUTER_API_KEY required",
                    "hardware": platform.platform(),
                    "run_count": 0,
                    "answer_provider": args.answer_provider,
                    "answer_model": args.answer_model,
                    "answer_prompt_sha256": prompt_hash,
                    "boundary": "Answer generation was not run; no end-to-end score is claimed.",
                },
            },
        )
        return

    dataset = read_json(args.dataset)
    rankings = {
        str(item["question_id"]): list(item.get("ranked_turn_ids", []))
        for item in retrieval.get("raw", {}).get("queries", [])
    }
    rows = dataset[: args.query_limit or None]
    hypotheses_path = Path(args.hypotheses)
    hypotheses_path.parent.mkdir(parents=True, exist_ok=True)
    latencies: list[int] = []
    with hypotheses_path.open("w", encoding="utf-8") as target:
        for row in rows:
            question_id = str(row["question_id"])
            prompt = build_prompt(row, rankings.get(question_id, []), args.max_sessions)
            try:
                answer, latency_ms = post_openrouter(api_key, args.answer_model, prompt)
            except (urllib.error.URLError, TimeoutError, KeyError, ValueError) as error:
                answer = f"I do not know. Answer generation failed: {type(error).__name__}."
                latency_ms = 180_000
            latencies.append(latency_ms)
            target.write(json.dumps({"question_id": question_id, "hypothesis": answer}) + "\n")

    write_json(
        args.result,
        {
            "schema_version": "1.0",
            "system": "WizeMe",
            "status": "partial",
            "dataset": retrieval["dataset"],
            "evaluation": {
                "task": "long-term-memory-qa",
                "mode": "end_to_end_qa",
                "granularity": "answer",
                "metric_definition": "Hypotheses generated from WizeMe retrieval. Official LongMemEval gpt-4o judging remains a separate pinned step.",
                "evaluator_revision": retrieval["evaluation"]["evaluator_revision"],
            },
            "metrics": {
                "hypothesis_count": len(rows),
                "answer_latency_mean_ms": round(sum(latencies) / max(1, len(latencies)), 3),
                "official_qa_score": None,
            },
            "provenance": {
                "generated_at": now_iso(),
                "source": "scripts/run_longmemeval_e2e.py",
                "command": " ".join(os.sys.argv),
                "hardware": platform.platform(),
                "run_count": 1,
                "answer_provider": args.answer_provider,
                "answer_model": args.answer_model,
                "answer_prompt_sha256": prompt_hash,
                "retrieval_artifact": str(Path(args.retrieval).resolve()),
                "hypotheses_artifact": str(hypotheses_path.resolve()),
                "boundary": "This artifact is incomplete until the pinned official evaluator writes its score.",
            },
        },
    )


if __name__ == "__main__":
    main()
