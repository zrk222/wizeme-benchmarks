# Memory Benchmark Comparison

Generated: 2026-06-23T18:54:48.582779Z

Only rows inside the same comparison group are directly comparable.

## LongMemEval / longmemeval-s-cleaned-turn

Revision: `98d7416c24c778c2fee6e6f3006e7a073259d48f` | Task: `long-term-memory-qa` | Mode: `end_to_end_qa` | Granularity: `answer`

| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |
|---|---|---:|---:|---:|---:|---|---|
| Mem0 | not_run | n/a | n/a | n/a | 0 | public | This is a matched same-mode placeholder. It is not a score; publish only after the provider writes hypotheses and the pinned official judge runs. |
| MemGPT | not_run | n/a | n/a | n/a | 0 | public | This is a matched same-mode placeholder. It is not a score; publish only after the provider writes hypotheses and the pinned official judge runs. |
| Supermemory | not_run | n/a | n/a | n/a | 0 | public | This is a matched same-mode placeholder. It is not a score; publish only after the provider writes hypotheses and the pinned official judge runs. |
| WizeMe | partial | n/a | n/a | n/a | 0 | public | Hypotheses may exist, but the official LongMemEval gpt-4o judge was not run. |

> No complete competitor receipt matches this dataset, revision, mode, and metric definition.

## LoCoMo / locomo10-dialog-turn

Revision: `3eb6f2c585f5e1699204e3c3bdf7adc5c28cb376` | Task: `evidence-retrieval` | Mode: `retrieval` | Granularity: `turn`

| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |
|---|---|---:|---:|---:|---:|---|---|
| WizeMe | complete | 0.6428 | n/a | 6.79 | 6 | public |  |

> No complete competitor receipt matches this dataset, revision, mode, and metric definition.

## LongMemEval / longmemeval-s-cleaned-turn

Revision: `98d7416c24c778c2fee6e6f3006e7a073259d48f` | Task: `evidence-retrieval` | Mode: `retrieval` | Granularity: `turn`

| System | Status | Primary score | FAMA | p95 ms | Runs | Evidence | Boundary |
|---|---|---:|---:|---:|---:|---|---|
| WizeMe | complete | 0.9255 | n/a | 9.20 | 6 | public |  |

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
