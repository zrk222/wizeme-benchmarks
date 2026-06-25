# Public Dissemination Status - 2026-06-25

## Published From This Repository

- GitHub repository: public benchmark receipts, methods, claim policy, comparison tables, machine-readable JSON, and audience-specific memory lift reports.
- GitHub Pages: public research index at `https://zrk222.github.io/wizeme-benchmarks/`.
- GitHub release: intended release target `memory-benchmarks-2026-06-25` with raw retrieval receipts and machine-readable report artifacts.

## Prepared But Account-Side

- Product Hunt: WizeMe launch payload and first-comment copy are prepared, but Product Hunt publication still requires the logged-in founder account and a live Product Hunt URL or screenshot receipt.
- LinkedIn: use `comparison/memory-lift-report-investor-2026.06.25.md` plus the bounded claim language in `comparison/CLAIMS.md`.
- Hugging Face: publish only the benchmark repo metadata, result receipts, and optional Space; do not publish proprietary WizeMe implementation internals.
- Zenodo: archive the GitHub release for a DOI after the release is visible.
- Papers with Code / arXiv: defer until a paper-style reproducibility package exists with same-mode provider rows or a clearly scoped WizeMe-only methods paper.

## Boundary

LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. Both are reported raw without cross-benchmark normalization.
