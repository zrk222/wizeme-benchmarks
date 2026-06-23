from __future__ import annotations

import argparse
import platform
from pathlib import Path

from common import now_iso, write_json


DATASET = {
    "name": "LongMemEval",
    "variant": "longmemeval-s-cleaned-turn",
    "revision": "98d7416c24c778c2fee6e6f3006e7a073259d48f",
    "sha256": "d6f21ea9d60a0d56f34a05b609c79c88a451d2ae03597821ea3d5a9678c3a442",
    "kind": "public",
}

EVALUATION = {
    "task": "long-term-memory-qa",
    "mode": "end_to_end_qa",
    "granularity": "answer",
    "metric_definition": "Official LongMemEval answer generation plus the unmodified official gpt-4o judge.",
    "evaluator_revision": "9e0b455f4ef0e2ab8f2e582289761153549043fc",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--system", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--reason", default="Provider adapter command and credentials are not configured.")
    args = parser.parse_args()

    write_json(
        Path(args.output),
        {
            "schema_version": "1.0",
            "system": args.system,
            "status": "not_run",
            "dataset": DATASET,
            "evaluation": EVALUATION,
            "metrics": {},
            "provenance": {
                "generated_at": now_iso(),
                "source": "scripts/write_pending_longmemeval_provider_qa.py",
                "command": args.reason,
                "hardware": platform.platform(),
                "run_count": 0,
                "boundary": (
                    "This is a matched same-mode placeholder. It is not a score; "
                    "publish only after the provider writes hypotheses and the pinned official judge runs."
                ),
            },
        },
    )


if __name__ == "__main__":
    main()
