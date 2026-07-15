from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
from pathlib import Path


SECRET = re.compile(
    rb"(?<![A-Za-z0-9])(?:sk-or-v1-[A-Za-z0-9_-]{20,}|m0-[A-Za-z0-9_-]{20,}|z_[A-Za-z0-9_-]{40,}(?:\.[A-Za-z0-9_-]{20,})?)"
)
RIGHT_OF_REPLY = {"not_applicable", "response_received", "window_elapsed", "owner_waived"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_slug(value: str) -> str:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise ValueError("slug must contain lowercase letters, numbers, and single hyphens")
    return value


def verified_bundle(bundle: Path) -> tuple[dict, list[Path]]:
    manifest_path = bundle / "manifest.json"
    if not manifest_path.is_file():
        raise ValueError("bundle manifest.json is missing")
    manifest = load_json(manifest_path)
    files = [manifest_path]
    for entry in manifest.get("artifacts", []):
        name = str(entry.get("file", ""))
        source = (bundle / name).resolve()
        if not name or source.parent != bundle.resolve() or not source.is_file():
            raise ValueError(f"invalid or missing artifact: {name}")
        data = source.read_bytes()
        if digest(data) != entry.get("sha256"):
            raise ValueError(f"SHA-256 mismatch: {name}")
        if SECRET.search(data):
            raise ValueError(f"secret-like value found: {name}")
        files.append(source)
    if len(files) < 2:
        raise ValueError("bundle manifest has no artifacts")
    return manifest, files


def verified_authorization(path: Path, manifest_path: Path) -> dict:
    authorization = load_json(path)
    if authorization.get("schemaVersion") != "wizeme_benchmark_publication_authorization_v1":
        raise ValueError("publication authorization schema is invalid")
    if authorization.get("authorized") is not True:
        raise ValueError("publication is not authorized")
    if authorization.get("bundleManifestSha256") != digest(manifest_path.read_bytes()):
        raise ValueError("publication authorization is not bound to this bundle")
    reply_status = authorization.get("rightOfReply", {}).get("status")
    if reply_status not in RIGHT_OF_REPLY:
        raise ValueError("right-of-reply status is missing or invalid")
    if reply_status != "not_applicable" and not authorization.get("rightOfReply", {}).get("evidence"):
        raise ValueError("competitor publication requires right-of-reply evidence")
    return authorization


def render_index(entries: list[dict]) -> str:
    items = "\n".join(
        f'<li><a href="{html.escape(item["slug"])}/">{html.escape(item["title"])}</a>'
        f' <small>{html.escape(item["publishedAt"])}</small></li>'
        for item in entries
    ) or "<li>No public competitor receipt has cleared the publication gate.</li>"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>WizeMe Benchmark Receipts</title><meta name="description" content="Hash-verified public benchmark receipts and reproduction artifacts.">
<style>body{{font:16px/1.6 system-ui;margin:0;color:#172229}}main{{width:min(900px,calc(100% - 32px));margin:64px auto}}a{{color:#087f8c}}li{{margin:12px 0}}small{{color:#5b6870}}</style></head>
<body><main><h1>Benchmark receipts</h1><p>Only hash-verified bundles with explicit publication authorization appear here.</p><ul>{items}</ul></main></body></html>"""


def publish(bundle: Path, authorization_path: Path, slug: str, title: str, output_root: Path, public_base: str) -> Path:
    manifest, files = verified_bundle(bundle)
    authorization = verified_authorization(authorization_path, bundle / "manifest.json")
    target = output_root / safe_slug(slug)
    if target.exists():
        raise ValueError(f"receipt already exists: {target}")
    target.mkdir(parents=True)
    for source in files:
        shutil.copy2(source, target / source.name)
    shutil.copy2(authorization_path, target / "publication-authorization.json")
    public_manifest = {
        "schemaVersion": "wizeme_public_receipt_v1",
        "slug": slug,
        "title": title,
        "publishedAt": authorization["authorizedAt"],
        "sourceManifestSha256": digest((bundle / "manifest.json").read_bytes()),
        "publicationAuthorizationSha256": digest(authorization_path.read_bytes()),
        "publicUrl": f"{public_base.rstrip('/')}/{slug}/",
        "artifacts": [
            {"file": source.name, "sha256": digest(source.read_bytes()), "url": f"{public_base.rstrip('/')}/{slug}/{source.name}"}
            for source in files
        ],
        "claimBoundary": authorization.get("claimBoundary", ""),
    }
    (target / "public-manifest.json").write_text(json.dumps(public_manifest, indent=2) + "\n", encoding="utf-8")
    links = "\n".join(
        f'<li><a href="{html.escape(item["file"])}">{html.escape(item["file"])}</a> <code>{item["sha256"]}</code></li>'
        for item in public_manifest["artifacts"]
    )
    (target / "index.html").write_text(
        f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{html.escape(title)}</title></head><body><main><h1>{html.escape(title)}</h1>'
        f'<p>{html.escape(public_manifest["claimBoundary"])}</p><ul>{links}</ul></main></body></html>',
        encoding="utf-8",
    )
    index_path = output_root / "index.json"
    entries = load_json(index_path).get("receipts", []) if index_path.exists() else []
    entries.append({key: public_manifest[key] for key in ("slug", "title", "publishedAt", "publicUrl")})
    entries.sort(key=lambda item: item["publishedAt"], reverse=True)
    index_path.write_text(json.dumps({"schemaVersion": "wizeme_public_receipt_index_v1", "receipts": entries}, indent=2) + "\n", encoding="utf-8")
    (output_root / "index.html").write_text(render_index(entries), encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", required=True, type=Path)
    parser.add_argument("--authorization", required=True, type=Path)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--output-root", type=Path, default=Path("docs/receipts"))
    parser.add_argument("--public-base", default="https://zrk222.github.io/wizeme-benchmarks/receipts")
    args = parser.parse_args()
    target = publish(args.bundle, args.authorization, args.slug, args.title, args.output_root, args.public_base)
    print(json.dumps({"status": "published", "path": str(target)}))


if __name__ == "__main__":
    main()
