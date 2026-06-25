# WizeMe Memory Benchmark Receipts - 2026-06-25

This release publishes refreshed public retrieval receipts for WizeMe memory evaluation.

## Current Public Retrieval Gates

- LoCoMo dialog-turn retrieval accuracy route: Recall Any@3 `0.7124` (`71.24%`), Recall All@3 `0.6070` (`60.70%`), Recall All@50 `0.8042` (`80.42%`), warm p95 `17.159 ms`, cold p95 `422.520 ms`.
- LoCoMo dialog-turn fast route: Recall Any@3 `0.7079` (`70.79%`), warm p95 `8.625 ms`, cold p95 `455.423 ms`.
- LongMemEval-S turn retrieval: Recall Any@3 `0.9255` (`92.55%`), raw-turn Recall All@3 `0.0362` (`3.62%`), answer-cluster/session All@3 ceiling `0.9319` (`93.19%`), warm p95 `11.005 ms`, cold p95 `13.094 ms`.

## Protocol Boundary

LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. Both are reported raw without cross-benchmark normalization.

## Included Artifacts

- `results/runs/wizeme/locomo/retrieval-turn.json`
- `results/runs/wizeme/longmemeval/retrieval-turn.json`
- `results/wizeme-memory-lift-2026-06-25.json`
- `comparison/memory-lift-report-engineer-2026.06.25.md`
- `comparison/memory-lift-report-investor-2026.06.25.md`
- `comparison/memory-lift-report-committee-2026.06.25.md`
- `comparison/latest.md`
- `comparison/CLAIMS.md`

These are retrieval gates, not end-to-end QA scores, medical advice, or public SOTA/provider superiority claims.
