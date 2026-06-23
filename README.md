# WizeMe Benchmarks

Reproducible, provenance-first evaluation for long-term conversational memory.

[![Benchmark](https://github.com/zrk222/wizeme-benchmarks/actions/workflows/benchmark.yml/badge.svg)](https://github.com/zrk222/wizeme-benchmarks/actions/workflows/benchmark.yml)
[![Research index](https://img.shields.io/badge/research-index-0b7285)](https://zrk222.github.io/wizeme-benchmarks/)
[![License: MIT](https://img.shields.io/badge/license-MIT-2f9e44.svg)](LICENSE)

**Keywords:** AI memory benchmark, conversational memory, long-term memory,
memory retrieval, LoCoMo, LongMemEval, PersonaMem, FAMA, forgetting-aware
accuracy, ANN, HNSW, pgvector, Mem0, Supermemory, MemGPT, Letta.

This repository compares systems only when they ran the same dataset, task,
metric definition, and evaluation mode. Missing competitor runs remain
`not_run`; they are never converted into zeroes or marketing claims.

- [Public benchmark index](https://zrk222.github.io/wizeme-benchmarks/)
- [Latest comparison report](comparison/latest.md)
- [Machine-readable comparison](results/comparison-latest.json)
- [How to submit a system result](CONTRIBUTING.md)
- [Citation metadata](CITATION.cff)

## Current Evidence

The repository now includes public retrieval receipts and the original
synthetic regression receipt:

| Lane | Recall Any@3 | FAMA | Warm p95 |
|---|---:|---:|---:|
| LoCoMo dialog-turn retrieval | 0.6473 | n/a | 177.497 ms |
| LongMemEval-S turn retrieval | 0.9319 | n/a | 16.816 ms |
| Semantic ANN | 1.0000 | n/a | 15.66 ms end-to-end |
| Long-term continuity fixture | 1.0000 | 1.0000 | 1.58 ms |

The LoCoMo and LongMemEval values are complete public-dataset retrieval runs
with three cold and three warm timed passes, not end-to-end QA scores. LoCoMo
uses a pinned local cross-encoder after hybrid candidate generation.
LongMemEval uses session-first lexical retrieval with protected top-three turn
localization and post-rank sibling evidence expansion. The synthetic values
remain regression evidence and are never mixed into public comparison groups.

See [the public methods](comparison/METHODS.md), [the exact experiment
profile](experiments/wizeme-public-retrieval-v1.json), and the raw receipts:

- `results/runs/wizeme/locomo/retrieval-turn.json`
- `results/runs/wizeme/longmemeval/retrieval-turn.json`

## Quick Start

```bash
python scripts/validate_results.py
python scripts/generate_comparison_report.py
docker compose up --build wizeme-benchmark comparison-report
```

Fetch public benchmark data into the ignored `datasets/cache/` directory:

```bash
python scripts/fetch_datasets.py --dataset locomo
python scripts/fetch_datasets.py --dataset longmemeval-s
python scripts/fetch_datasets.py --dataset personamem-32k
```

Dataset licenses and terms remain with their publishers. Review them before
redistribution or commercial use.

## Run A System

Every adapter must produce `benchmark-result.schema.json`.

```bash
python scripts/run_external.py \
  --system mem0 \
  --command "python /adapter/run.py" \
  --output results/runs/mem0.json
```

The wrapped command must write a normalized JSON result to the path in
`BENCHMARK_OUTPUT`. Optional Docker competitor services are enabled with:

```bash
docker compose --profile competitors up --build
```

Provide `SUPERMEMORY_COMMAND`, `MEM0_COMMAND`, or `MEMGPT_COMMAND`; an absent
command produces an honest `not_run` receipt.

## Publication Gate

Claims such as “0.91 vs 0.95,” “3.96 ms vs seconds,” or “perfect long-term
memory” require:

1. Same public dataset and pinned revision.
2. Same task and metric definition.
3. Same retrieval or end-to-end evaluation mode.
4. Raw result artifact and hardware/runtime metadata.
5. At least three timed runs for latency, with warm/cold state disclosed.

Until those conditions pass, use: “WizeMe’s synthetic regression suite reached
1.0 Recall@3 and 1.0 FAMA; public benchmark comparison is in progress.”

## Sources

- [LoCoMo official repository](https://github.com/snap-research/locomo)
- [LongMemEval official repository](https://github.com/xiaowu0162/LongMemEval)
- [PersonaMem official repository](https://github.com/bowen-upenn/PersonaMem)

## Research Discovery

The repository exposes citation metadata, CodeMeta, JSON result receipts,
GitHub topics, a sitemap, and a GitHub Pages research index. Public benchmark
receipts can be proposed through an issue or pull request using the normalized
schema. See [DISCOVERY.md](DISCOVERY.md) for indexing and dissemination routes.

## Layout

- `datasets/`: manifests and acquisition metadata
- `scripts/`: fetch, adapter, validation, and report tooling
- `results/`: normalized result receipts and generated reports
- `comparison/`: publication tables and claim policy
- `.github/workflows/benchmark.yml`: scheduled and push CI

## Citation

```bibtex
@software{wizeme_benchmarks_2026,
  title = {WizeMe Benchmarks: Reproducible Long-Term Memory Evaluation},
  author = {WizeMe},
  year = {2026},
  url = {https://github.com/zrk222/wizeme-benchmarks}
}
```
