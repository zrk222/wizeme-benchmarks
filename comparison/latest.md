# Memory Benchmark Comparison

Generated: 2026-07-16T06:21:38.604852Z

Only rows inside the same comparison group are directly comparable.

LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. Both are reported without cross-benchmark normalization.

## LongMemEval / longmemeval-s-cleaned-turn

Revision: `98d7416c24c778c2fee6e6f3006e7a073259d48f` | Task: `long-term-memory-qa` | Mode: `end_to_end_qa` | Granularity: `answer`

| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |
|---|---|---:|---:|---:|---:|---|---|
| Mem0 | not_run | n/a | n/a | n/a | 0 | public | This is a matched same-mode placeholder. It is not a score; publish only after the provider writes hypotheses and the pinned official judge runs. |
| MemGPT | not_run | n/a | n/a | n/a | 0 | public | This is a matched same-mode placeholder. It is not a score; publish only after the provider writes hypotheses and the pinned official judge runs. |
| Supermemory | not_run | n/a | n/a | n/a | 0 | public | This is a matched same-mode placeholder. It is not a score; publish only after the provider writes hypotheses and the pinned official judge runs. |
| WizeMe | partial | n/a | n/a | n/a | 0 | public | Hypotheses may exist, but the official LongMemEval gpt-4o judge was not run. |

> No complete competitor receipt matches this dataset, revision, mode, and metric definition.

## LoCoMo / locomo10-e2e-qa-300

Revision: `3eb6f2c585f5e1699204e3c3bdf7adc5c28cb376` | Task: `answer-quality` | Mode: `end_to_end_qa` | Granularity: `question`

| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |
|---|---|---:|---:|---:|---:|---|---|
| WizeMe | complete | 0.8367 | n/a | 14630.00 | 3 | public | Three complete 300-question all-category runs. Core Categories 1-4 and adversarial Category 5 are disclosed separately. Not a full-dataset or same-mode provider leaderboard result. |
| WizeMe prior gate | complete | 0.7333 | n/a | 7524.00 | 1 | public | Historical prior scoped 300-question gate. It predates the three-run dual quality lane and is not a same-run control. |

## LoCoMo / locomo10-dialog-turn

Revision: `3eb6f2c585f5e1699204e3c3bdf7adc5c28cb376` | Task: `evidence-retrieval` | Mode: `retrieval` | Granularity: `turn`

| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |
|---|---|---:|---:|---:|---:|---|---|
| WizeMe | complete | 0.7124 | n/a | 17.16 | 6 | public | Retrieval metric only. This row is not an end-to-end QA score. |

> No complete competitor receipt matches this dataset, revision, mode, and metric definition.

## LongMemEval / longmemeval-s-cleaned-turn

Revision: `98d7416c24c778c2fee6e6f3006e7a073259d48f` | Task: `evidence-retrieval` | Mode: `retrieval` | Granularity: `turn`

| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |
|---|---|---:|---:|---:|---:|---|---|
| WizeMe | complete | 0.9319 | n/a | 13.38 | 6 | public | Benchmark-specific retrieval metric; not cross-normalized with LoCoMo. |

> No complete competitor receipt matches this dataset, revision, mode, and metric definition.

## WizeMe memory regression suite / synthetic-2026-06-23

Revision: `2026-06-23T05:13:35.746Z` | Task: `retrieval-continuity-forgetting` | Mode: `retrieval` | Granularity: ``

| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |
|---|---|---:|---:|---:|---:|---|---|
| WizeMe | complete | 1.0000 | 1.0000 | 15.66 | 1 | synthetic | Synthetic regression evidence only; not a public LoCoMo, LongMemEval, or PersonaMem score. |

> No complete competitor receipt matches this dataset, revision, mode, and metric definition.

## Pending Adapters

| System | Status | Reason |
|---|---|---|
| Mem0 | not_run | scripts/write_pending_longmemeval_provider_qa.py |
| mem0 | not_run | Adapter command is not configured. |
| MemGPT | not_run | scripts/write_pending_longmemeval_provider_qa.py |
| memgpt | not_run | Adapter command is not configured. |
| Supermemory | not_run | scripts/write_pending_longmemeval_provider_qa.py |
| supermemory | not_run | Adapter command is not configured. |
| WizeMe | partial | scripts/run_longmemeval_e2e.py |

## Publication Boundary

Synthetic receipts validate regression behavior, not public benchmark leadership. Latency comparisons require matching hardware, warm/cold state, timing boundary, and at least three runs.
