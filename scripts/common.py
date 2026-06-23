from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def read_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: str | Path, value: dict[str, Any]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def not_run_result(system: str, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "system": system,
        "status": "not_run",
        "dataset": {
            "name": "unassigned",
            "variant": "unassigned",
            "revision": "unassigned",
            "kind": "public",
        },
        "evaluation": {
            "task": "unassigned",
            "mode": "retrieval",
            "metric_definition": "No adapter command configured.",
        },
        "metrics": {},
        "provenance": {
            "generated_at": now_iso(),
            "source": reason,
            "command": "",
            "hardware": "not captured",
            "run_count": 0,
        },
    }

