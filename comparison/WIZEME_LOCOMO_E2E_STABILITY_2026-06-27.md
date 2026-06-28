# LoCoMo E2E QA Quality-Lane Stability Receipt

Generated: 2026-06-28T02:39:24.553Z

- Runs: 3 x 300 questions
- Dataset SHA-256: `79fa87e90f04081343b8c8debecb80a9a6842b76a7aa537dc9fdf651ea698ff4`
- Core Categories 1-4 mean: 87.30% (range 87.01-87.45%)
- All-category mean: 83.67% (range 83.00-84.00%)
- Adversarial Category 5 mean: 71.50% (range 68.12-73.91%)
- Answer p95 mean: 14052.33 ms (range 13702-14630 ms)
- Conservative published answer p95: 14630 ms

## Boundary

- Three deterministic 300-question WizeMe harness runs. Not the full 1,982-question LoCoMo E2E gate and not a same-mode provider row.
- Core Categories 1-4 and adversarial Category 5 are reported separately.
- Retrieval latency remains separate from answer-model and judge latency.
- Public aggregate receipts contain no private user data, secrets, or non-public ranking internals.
