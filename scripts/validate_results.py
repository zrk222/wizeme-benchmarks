from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from common import read_json


REQUIRED = ("schema_version", "system", "status", "dataset", "evaluation", "metrics", "provenance")


def validate(result: dict[str, Any], path: Path) -> list[str]:
    errors = [f"{path}: missing {key}" for key in REQUIRED if key not in result]
    if result.get("schema_version") != "1.0":
        errors.append(f"{path}: schema_version must be 1.0")
    if result.get("status") not in {"complete", "partial", "not_run", "failed"}:
        errors.append(f"{path}: invalid status")
    if result.get("status") == "complete":
        for key in ("name", "variant", "revision", "kind"):
            if not result.get("dataset", {}).get(key):
                errors.append(f"{path}: dataset.{key} is required")
        for key in ("generated_at", "source", "command", "hardware", "run_count"):
            if key not in result.get("provenance", {}):
                errors.append(f"{path}: provenance.{key} is required")
        if result.get("dataset", {}).get("kind") == "public":
            dataset = result.get("dataset", {})
            evaluation = result.get("evaluation", {})
            provenance = result.get("provenance", {})
            raw = result.get("raw", {})
            if len(str(dataset.get("revision", ""))) != 40:
                errors.append(f"{path}: public dataset revision must be an immutable 40-character commit")
            if len(str(dataset.get("sha256", ""))) != 64:
                errors.append(f"{path}: public dataset sha256 is required")
            for key in ("evaluator_revision", "granularity"):
                if not evaluation.get(key):
                    errors.append(f"{path}: evaluation.{key} is required for public results")
            if evaluation.get("mode") == "retrieval":
                if provenance.get("run_count", 0) < 6:
                    errors.append(f"{path}: public latency publication requires at least 6 runs")
                if provenance.get("cold_run_count", 0) < 3 or provenance.get("warm_run_count", 0) < 3:
                    errors.append(f"{path}: public retrieval results require at least 3 cold and 3 warm runs")
                if not provenance.get("cache_disclosure"):
                    errors.append(f"{path}: provenance.cache_disclosure is required")
            if not isinstance(provenance.get("hardware"), dict):
                errors.append(f"{path}: public hardware metadata must be structured")
            if not provenance.get("aggregate_public_receipt") and (not raw.get("runs") or not raw.get("queries")):
                errors.append(f"{path}: raw runs and per-query artifacts are required")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", default="results/runs")
    args = parser.parse_args()
    paths = sorted(Path(args.results).rglob("*.json"))
    if not paths:
        raise SystemExit("No result JSON files found.")
    errors: list[str] = []
    for path in paths:
        errors.extend(validate(read_json(path), path))
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(paths)} result file(s).")


if __name__ == "__main__":
    main()
