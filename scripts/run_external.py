from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

from common import not_run_result, read_json, write_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--system", required=True)
    parser.add_argument("--command", default="")
    parser.add_argument("--command-env", default="")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    command = args.command or (os.environ.get(args.command_env, "") if args.command_env else "")
    if not command.strip():
        write_json(args.output, not_run_result(args.system, "Adapter command is not configured."))
        return

    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["BENCHMARK_OUTPUT"] = str(output)
    completed = subprocess.run(command, shell=True, env=env, check=False)
    if completed.returncode != 0:
        result = not_run_result(args.system, f"Adapter exited with code {completed.returncode}.")
        result["status"] = "failed"
        result["provenance"]["command"] = command
        write_json(output, result)
        raise SystemExit(completed.returncode)
    if not output.exists():
        raise SystemExit("Adapter succeeded but did not write BENCHMARK_OUTPUT.")
    result = read_json(output)
    if result.get("system", "").lower() != args.system.lower():
        raise SystemExit("Adapter result system does not match requested system.")


if __name__ == "__main__":
    main()

