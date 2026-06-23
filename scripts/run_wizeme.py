from __future__ import annotations

import argparse

from common import read_json, write_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="results/runs/wizeme.json")
    args = parser.parse_args()
    source = read_json(args.input)

    result = {
        "schema_version": "1.0",
        "system": "WizeMe",
        "status": "complete",
        "dataset": {
            "name": "WizeMe memory regression suite",
            "variant": "synthetic-2026-06-23",
            "revision": source["source_generated_at"],
            "kind": "synthetic",
        },
        "evaluation": {
            "task": "retrieval-continuity-forgetting",
            "mode": "retrieval",
            "metric_definition": (
                "Recall@3 retrieves relevant evidence in the first three results; "
                "FAMA penalizes retrieval of invalid or obsolete memories."
            ),
        },
        "metrics": {
            "recall_at_3": source["semantic_ann"]["recall_at_3"],
            "mrr_at_3": source["semantic_ann"]["mrr_at_3"],
            "latency_p95_ms": source["semantic_ann"]["latency_p95_ms"],
            "vector_path_p95_ms": source["semantic_ann"]["vector_path_p95_ms"],
            "cached_repeat_p95_ms": source["semantic_ann"]["cached_repeat_p95_ms"],
            "long_term_recall_at_3": source["long_term"]["recall_at_3"],
            "fama": source["long_term"]["fama"],
            "long_term_latency_p95_ms": source["long_term"]["latency_p95_ms"],
            "persona_recall_at_3": source["persona_memora"]["recall_at_3"],
            "persona_fama": source["persona_memora"]["fama"],
        },
        "provenance": {
            "generated_at": source["source_generated_at"],
            "source": source["source"],
            "command": "pnpm benchmark:memory-retrieval",
            "hardware": source["hardware"],
            "run_count": 1,
            "boundary": source["boundary"],
        },
    }
    write_json(args.output, result)


if __name__ == "__main__":
    main()

