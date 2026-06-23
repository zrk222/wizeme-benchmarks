from __future__ import annotations

import argparse
import hashlib
import time
import urllib.request
import urllib.error
from pathlib import Path

from common import read_json, write_json


def download(url: str, output: Path, expected_sha256: str | None = None) -> dict[str, object]:
    output.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    size = 0
    request = urllib.request.Request(url, headers={"User-Agent": "wizeme-benchmarks/0.1"})
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            digest = hashlib.sha256()
            size = 0
            with urllib.request.urlopen(request, timeout=120) as response, output.open("wb") as target:
                while chunk := response.read(1024 * 1024):
                    target.write(chunk)
                    digest.update(chunk)
                    size += len(chunk)
            last_error = None
            break
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            last_error = error
            output.unlink(missing_ok=True)
            if attempt < 3:
                time.sleep(2 ** (attempt - 1))
    if last_error is not None:
        raise SystemExit(f"Download failed after 3 attempts for {url}: {last_error}")
    actual_sha256 = digest.hexdigest()
    if expected_sha256 and actual_sha256.lower() != expected_sha256.lower():
        output.unlink(missing_ok=True)
        raise SystemExit(
            f"Checksum mismatch for {url}: expected {expected_sha256}, got {actual_sha256}"
        )
    return {
        "path": str(output),
        "bytes": size,
        "sha256": actual_sha256,
        "expected_sha256": expected_sha256,
        "verified": bool(expected_sha256),
        "url": url,
    }


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
        download(
            item["url"],
            Path(args.cache) / item["output"],
            item.get("sha256") or entry.get("sha256"),
        )
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
