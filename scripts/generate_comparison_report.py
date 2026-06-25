from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from common import now_iso, read_json, write_json


def comparison_key(result: dict[str, Any]) -> tuple[str, ...]:
    dataset = result["dataset"]
    evaluation = result["evaluation"]
    return (
        dataset["name"],
        dataset["variant"],
        dataset["revision"],
        evaluation.get("task", ""),
        evaluation["mode"],
        evaluation.get("granularity", ""),
        evaluation.get("evaluator_revision", ""),
        evaluation["metric_definition"],
    )


def metric(value: Any, digits: int = 4) -> str:
    return "n/a" if value is None else f"{float(value):.{digits}f}"


def primary_metrics(row: dict[str, Any]) -> tuple[Any, Any, Any]:
    metrics = row["metrics"]
    if row.get("evaluation", {}).get("mode") == "end_to_end_qa":
        return (
            metrics.get("official_qa_score"),
            None,
            metrics.get("answer_latency_p95_ms") or metrics.get("answer_latency_mean_ms"),
        )
    if "turn" in metrics:
        return (
            metrics["turn"].get("recall_any@3"),
            metrics.get("fama"),
            metrics.get("warm_latency", {}).get("p95_ms"),
        )
    return metrics.get("recall_at_3"), metrics.get("fama"), metrics.get("latency_p95_ms")


def main() -> None:
    result_paths = sorted(Path("results/runs").rglob("*.json"))
    results = [read_json(path) for path in result_paths]
    complete = [result for result in results if result.get("status") == "complete"]
    assigned = [
        result
        for result in results
        if result.get("dataset", {}).get("revision") not in {"", "unassigned", None}
        and result.get("evaluation", {}).get("task") not in {"", "unassigned", None}
    ]
    groups: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for result in assigned:
        groups[comparison_key(result)].append(result)

    lines = [
        "# Memory Benchmark Comparison",
        "",
        f"Generated: {now_iso()}",
        "",
        "Only rows inside the same comparison group are directly comparable.",
        "",
        "LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 "
        "measures exact-turn retrieval across 272 tightly clustered sessions. "
        "LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. "
        "Both are reported raw without cross-benchmark normalization.",
        "",
    ]
    for key, rows in groups.items():
        lines.extend(
            [
                f"## {key[0]} / {key[1]}",
                "",
                f"Revision: `{key[2]}` | Task: `{key[3]}` | Mode: `{key[4]}` | Granularity: `{key[5]}`",
                "",
                "| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |",
                "|---|---|---:|---:|---:|---:|---|---|",
            ]
        )
        for row in rows:
            recall, fama, p95 = primary_metrics(row)
            lines.append(
                "| {system} | {status} | {recall} | {fama} | {p95} | {runs} | {kind} | {boundary} |".format(
                    system=row["system"],
                    status=row["status"],
                    recall=metric(recall),
                    fama=metric(fama),
                    p95=metric(p95, 2),
                    runs=row["provenance"]["run_count"],
                    kind=row["dataset"]["kind"],
                    boundary=str(row.get("provenance", {}).get("boundary", "")).replace("|", "/"),
                )
            )
        lines.append("")
        complete_rows = [row for row in rows if row.get("status") == "complete"]
        if len(complete_rows) < 2:
            lines.extend(
                [
                    "> No complete competitor receipt matches this dataset, revision, mode, and metric definition.",
                    "",
                ]
            )

    pending = [result for result in results if result.get("status") != "complete"]
    if pending:
        lines.extend(["## Pending Adapters", "", "| System | Status | Reason |", "|---|---|---|"])
        for row in pending:
            lines.append(
                f"| {row['system']} | {row['status']} | {row['provenance']['source']} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Publication Boundary",
            "",
            "Synthetic receipts validate regression behavior, not public benchmark leadership. "
            "Latency comparisons require matching hardware, warm/cold state, timing boundary, and at least three runs.",
            "",
        ]
    )
    Path("comparison").mkdir(parents=True, exist_ok=True)
    Path("comparison/latest.md").write_text("\n".join(lines), encoding="utf-8")
    write_json(
        "results/comparison-latest.json",
        {
            "generated_at": now_iso(),
            "comparison_group_count": len(groups),
            "complete_result_count": len(complete),
            "pending_result_count": len(pending),
            "groups": [
                {"key": list(key), "systems": [row["system"] for row in rows]}
                for key, rows in groups.items()
            ],
        },
    )
    print(json.dumps({"groups": len(groups), "complete": len(complete), "pending": len(pending)}))


if __name__ == "__main__":
    main()
