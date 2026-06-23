from __future__ import annotations

import argparse
import hashlib
import urllib.request
from pathlib import Path

from common import read_json, write_json


def download(url: str, output: Path) -> dict[str, object]:
    output.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(url, timeout=120) as response, output.open("wb") as target:
        while chunk := response.read(1024 * 1024):
            target.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    return {"path": str(output), "bytes": size, "sha256": digest.hexdigest(), "url": url}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--catalog", default="datasets/manifests/catalog.json")
    parser.add_argument("--cache", default="datasets/cache")
    args = parser.parse_args()

    catalog = read_json(args.catalog)
    if args.dataset not in catalog:
        raise SystemExit(f"Unknown dataset: {args.dataset}")
    entry = catalog[args.dataset]
    files = entry.get("files") or [{"url": entry["url"], "output": entry["output"]}]
    receipts = [
        download(item["url"], Path(args.cache) / item["output"])
        for item in files
    ]
    write_json(
        Path(args.cache) / args.dataset / "download-receipt.json",
        {
            "dataset": args.dataset,
            "publisher": entry["publisher"],
            "revision": entry["revision"],
            "source": entry["source"],
            "files": receipts,
        },
    )


if __name__ == "__main__":
    main()

