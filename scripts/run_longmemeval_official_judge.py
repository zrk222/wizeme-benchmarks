from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

from common import read_json, write_json


def run(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hypotheses", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--cache", default="datasets/cache/official/LongMemEval")
    args = parser.parse_args()

    result = read_json(args.result)
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        result["status"] = "partial"
        result["provenance"]["official_judge"] = "not_run: OPENAI_API_KEY required"
        result["provenance"]["boundary"] = (
            "Hypotheses may exist, but the official LongMemEval gpt-4o judge was not run."
        )
        write_json(args.result, result)
        return

    cache = Path(args.cache)
    if not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        run(["git", "clone", "https://github.com/xiaowu0162/LongMemEval.git", str(cache)])
    run(["git", "fetch", "--all", "--tags"], cwd=cache)
    run(["git", "checkout", "--detach", args.revision], cwd=cache)
    actual_revision = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=cache, text=True
    ).strip()
    if actual_revision != args.revision:
        raise SystemExit(f"Evaluator revision mismatch: {actual_revision}")

    evaluator_dir = cache / "src" / "evaluation"
    oracle = cache / "data" / "longmemeval_oracle.json"
    hypotheses = Path(args.hypotheses).resolve()
    judge_artifact = Path(f"{hypotheses}.eval-results-gpt-4o")
    run(
        [
            os.sys.executable,
            "evaluate_qa.py",
            "gpt-4o",
            str(hypotheses),
            str(oracle.resolve()),
        ],
        cwd=evaluator_dir,
    )
    labels = []
    by_type: dict[str, list[int]] = {}
    oracle_rows = json.loads(oracle.read_text(encoding="utf-8"))
    question_types = {
        str(row["question_id"]): str(row["question_type"])
        for row in oracle_rows
    }
    for line in judge_artifact.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        label = bool(row.get("autoeval_label", {}).get("label"))
        value = 1 if label else 0
        labels.append(value)
        question_type = question_types.get(str(row.get("question_id")), "unknown")
        by_type.setdefault(question_type, []).append(value)
    result["metrics"]["official_qa_score"] = round(sum(labels) / max(1, len(labels)), 4)
    result["metrics"]["official_qa_count"] = len(labels)
    result["metrics"]["official_qa_by_type"] = {
        key: {
            "accuracy": round(sum(values) / max(1, len(values)), 4),
            "count": len(values),
        }
        for key, values in sorted(by_type.items())
    }
    result["status"] = "complete"
    result["provenance"]["official_judge"] = {
        "model": "gpt-4o",
        "revision": actual_revision,
        "script": str((evaluator_dir / "evaluate_qa.py").resolve()),
        "oracle": str(oracle.resolve()),
        "raw_artifact": str(judge_artifact.resolve()),
    }
    result["provenance"]["boundary"] = (
        "Answer model and official judge are separately pinned and disclosed."
    )
    write_json(args.result, result)


if __name__ == "__main__":
    main()
