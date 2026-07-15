from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from publish_receipt_bundle import publish


class PublishReceiptBundleTest(unittest.TestCase):
    def test_verified_publish_and_tamper_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            bundle = root / "bundle"
            bundle.mkdir()
            artifact = bundle / "receipt.json"
            artifact.write_text('{"status":"complete"}\n', encoding="utf-8")
            manifest = {"artifacts": [{"file": artifact.name, "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest()}]}
            manifest_path = bundle / "manifest.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            authorization = root / "authorization.json"
            authorization.write_text(json.dumps({
                "schemaVersion": "wizeme_benchmark_publication_authorization_v1",
                "authorized": True,
                "authorizedAt": "2026-07-15T00:00:00Z",
                "bundleManifestSha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
                "rightOfReply": {"status": "window_elapsed", "evidence": "receipt-of-delivery.json"},
                "claimBoundary": "Matched internal reference.",
            }), encoding="utf-8")
            output = root / "docs" / "receipts"
            target = publish(bundle, authorization, "matched-locomo", "Matched LoCoMo", output, "https://example.test/receipts")
            self.assertTrue((target / "public-manifest.json").is_file())
            self.assertIn("matched-locomo", (output / "index.html").read_text(encoding="utf-8"))
            artifact.write_text("tampered", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
                publish(bundle, authorization, "tampered", "Tampered", output, "https://example.test/receipts")

    def test_owner_waiver_requires_public_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            bundle = root / "bundle"
            bundle.mkdir()
            artifact = bundle / "receipt.json"
            artifact.write_text('{"status":"complete"}\n', encoding="utf-8")
            manifest_path = bundle / "manifest.json"
            manifest_path.write_text(json.dumps({
                "artifacts": [{"file": artifact.name, "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest()}],
            }), encoding="utf-8")
            authorization = root / "authorization.json"
            base = {
                "schemaVersion": "wizeme_benchmark_publication_authorization_v1",
                "authorized": True,
                "authorizedAt": "2026-07-15T00:00:00Z",
                "bundleManifestSha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
                "claimBoundary": "Matched internal reference.",
            }
            authorization.write_text(json.dumps({
                **base,
                "rightOfReply": {"status": "owner_waived", "evidence": ""},
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "right-of-reply evidence"):
                publish(bundle, authorization, "missing-waiver", "Missing waiver", root / "out", "https://example.test")
            authorization.write_text(json.dumps({
                **base,
                "rightOfReply": {"status": "owner_waived", "evidence": "publication-boundary.md"},
            }), encoding="utf-8")
            target = publish(bundle, authorization, "owner-waived", "Owner waived", root / "out", "https://example.test")
            self.assertTrue((target / "public-manifest.json").is_file())


if __name__ == "__main__":
    unittest.main()
