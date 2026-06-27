# Public Retrieval Methods

## LoCoMo

- Dataset commit: `3eb6f2c585f5e1699204e3c3bdf7adc5c28cb376`
- File SHA-256: `79fa87e90f04081343b8c8debecb80a9a6842b76a7aa537dc9fdf651ea698ff4`
- Unit: one dialog turn per memory document
- Ground truth: annotated `qa[].evidence` dialog IDs
- Questions without evidence are excluded
- Metrics: Recall Any, Recall All, and nDCG
- Public receipts disclose outcomes, scope, timing boundaries, dataset hashes,
  and hardware metadata.
- Internal retrieval configuration and diagnostic traces are withheld.

## LongMemEval-S

- Dataset commit: `98d7416c24c778c2fee6e6f3006e7a073259d48f`
- Evaluator commit: `9e0b455f4ef0e2ab8f2e582289761153549043fc`
- File SHA-256: `d6f21ea9d60a0d56f34a05b609c79c88a451d2ae03597821ea3d5a9678c3a442`
- Unit: one user turn per memory document
- Abstention questions are excluded from retrieval metrics
- Ground truth and Recall Any/All/nDCG follow the official evaluator semantics

## Timing

Every published retrieval result contains three cold and three warm runs.
Aggregate public receipts disclose p95 latency and cache-state boundaries.
Detailed per-query traces are retained for controlled review because they can
reveal implementation configuration.

LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3
measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval
Any@3 measures answer-cluster retrieval across a larger haystack. Both are
reported raw without cross-benchmark normalization.

## End-to-End QA

Retrieval and answer quality are reported as separate modes. The pinned
LongMemEval end-to-end workflow writes `question_id` plus `hypothesis` JSONL
with a separately disclosed answer model. The unmodified official LongMemEval
`src/evaluation/evaluate_qa.py` script is then checked out at commit
`9e0b455f4ef0e2ab8f2e582289761153549043fc` and run with the official `gpt-4o`
judge and oracle. Missing answer or judge credentials produce `not_run` or
`partial`, never a substituted score.

The separate LoCoMo 300-question WizeMe QA harness reports judged accuracy,
an official-style mean, answer latency, and judge latency. It is clearly
labeled as a tuning gate and is not mixed with official provider rows.

Provider QA comparison rows for Supermemory, Mem0, and MemGPT are emitted as
matched `not_run` receipts under the same LongMemEval dataset revision,
evaluation mode, metric definition, and official judge revision. They are not
scores. They exist so the missing provider adapter work stays visible in the
same comparison group instead of being hidden in prose.
