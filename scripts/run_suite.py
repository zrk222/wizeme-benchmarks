from __future__ import annotations

import subprocess
import sys


COMMANDS = [
    [
        sys.executable,
        "scripts/run_wizeme.py",
        "--input",
        "datasets/manifests/wizeme-synthetic-regression.json",
        "--output",
        "results/runs/wizeme.json",
    ],
    [sys.executable, "scripts/validate_results.py"],
    [sys.executable, "scripts/generate_comparison_report.py"],
]


def main() -> None:
    for command in COMMANDS:
        subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
