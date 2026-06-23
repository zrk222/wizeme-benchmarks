# Memory Benchmark Comparison

Generated: 2026-06-23T09:07:12.398582Z

Only rows inside the same comparison group are directly comparable.

## LoCoMo / locomo10-dialog-turn

Revision: `3eb6f2c585f5e1699204e3c3bdf7adc5c28cb376` | Task: `evidence-retrieval` | Mode: `retrieval` | Granularity: `turn`

| System | Recall@3 | FAMA | p95 ms | Runs | Evidence |
|---|---:|---:|---:|---:|---|
| WizeMe | 0.6473 | n/a | 177.50 | 6 | public |

> No direct competitor receipt matches this dataset, revision, mode, and metric definition.

## LongMemEval / longmemeval-s-cleaned-turn

Revision: `98d7416c24c778c2fee6e6f3006e7a073259d48f` | Task: `evidence-retrieval` | Mode: `retrieval` | Granularity: `turn`

| System | Recall@3 | FAMA | p95 ms | Runs | Evidence |
|---|---:|---:|---:|---:|---|
| WizeMe | 0.9319 | n/a | 16.82 | 6 | public |

> No direct competitor receipt matches this dataset, revision, mode, and metric definition.

## WizeMe memory regression suite / synthetic-2026-06-23

Revision: `2026-06-23T05:13:35.746Z` | Task: `retrieval-continuity-forgetting` | Mode: `retrieval` | Granularity: ``

| System | Recall@3 | FAMA | p95 ms | Runs | Evidence |
|---|---:|---:|---:|---:|---|
| WizeMe | 1.0000 | 1.0000 | 15.66 | 1 | synthetic |

> No direct competitor receipt matches this dataset, revision, mode, and metric definition.

## Pending Adapters

| System | Status | Reason |
|---|---|---|
| mem0 | not_run | Adapter command is not configured. |
| memgpt | not_run | Adapter command is not configured. |
| supermemory | not_run | Adapter command is not configured. |

## Publication Boundary

Synthetic receipts validate regression behavior, not public benchmark leadership. Latency comparisons require matching hardware, warm/cold state, timing boundary, and at least three runs.
