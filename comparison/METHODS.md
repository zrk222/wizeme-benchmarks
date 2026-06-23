# Public Retrieval Methods

## LoCoMo

- Dataset commit: `3eb6f2c585f5e1699204e3c3bdf7adc5c28cb376`
- File SHA-256: `79fa87e90f04081343b8c8debecb80a9a6842b76a7aa537dc9fdf651ea698ff4`
- Unit: one dialog turn per memory document
- Ground truth: annotated `qa[].evidence` dialog IDs
- Questions without evidence are excluded
- Metrics: Recall Any, Recall All, and nDCG

## LongMemEval-S

- Dataset commit: `98d7416c24c778c2fee6e6f3006e7a073259d48f`
- Evaluator commit: `9e0b455f4ef0e2ab8f2e582289761153549043fc`
- File SHA-256: `d6f21ea9d60a0d56f34a05b609c79c88a451d2ae03597821ea3d5a9678c3a442`
- Unit: one user turn per memory document
- Abstention questions are excluded from retrieval metrics
- Ground truth and Recall Any/All/nDCG follow the official evaluator semantics

## Timing

Every published public result contains three cold and three warm runs. Raw
per-query latencies and rankings are retained. Index construction is included
in query latency. The local embedding model process remains loaded between
runs; cold runs clear embedding and document-vector caches.

## End-to-End QA

Retrieval and answer quality are reported as separate modes. The pinned
end-to-end profile is `experiments/wizeme-longmemeval-e2e-v1.json`.
WizeMe first writes `question_id` plus `hypothesis` JSONL with a separately
disclosed answer model. The unmodified official LongMemEval
`src/evaluation/evaluate_qa.py` script is then checked out at commit
`9e0b455f4ef0e2ab8f2e582289761153549043fc` and run with the official `gpt-4o`
judge and oracle. Missing answer or judge credentials produce `not_run` or
`partial`, never a substituted score.

Provider QA comparison rows for Supermemory, Mem0, and MemGPT are emitted as
matched `not_run` receipts under the same LongMemEval dataset revision,
evaluation mode, metric definition, and official judge revision. They are not
scores. They exist so the missing provider adapter work stays visible in the
same comparison group instead of being hidden in prose.
