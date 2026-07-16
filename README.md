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
- [Submit a reproducible benchmark issue](https://github.com/zrk222/wizeme-benchmarks/issues/new?template=benchmark-result.yml)
- [Scheduled benchmark workflow](https://github.com/zrk222/wizeme-benchmarks/actions/workflows/benchmark.yml)
- [Citation metadata](CITATION.cff)

## Current Evidence

Retrieval and end-to-end QA are separate metric families:

| Lane | Scope | Primary result | Supporting result | p95 |
|---|---|---:|---:|---:|
| LoCoMo retrieval | 1,982 questions | Any@3 0.7124 (71.24%) | All@3 0.6070 (60.70%) | 422.520/17.159 ms cold/warm |
| LoCoMo low-latency retrieval | 1,982 questions | Any@3 0.7109 (71.09%) | Any@15 0.8643 (86.43%) | 18.777/20.107 ms cold/warm |
| LongMemEval retrieval | 470 questions | Any@3 0.9319 (93.19%) | All@50 0.8489 (84.89%) | 11.827/13.382 ms cold/warm |
| LoCoMo E2E QA dual quality lane | 3 x 300 questions | All-category mean 0.8367 (83.67%) | Core Categories 1-4 mean 0.8730 (87.30%) | 14.630/12.893 s conservative answer/judge |
| LoCoMo E2E QA faster lane | 300 questions | All-category 0.8333 (83.33%) | Core Categories 1-4 0.8615 (86.15%) | 7.047/13.491 s answer/judge |

The all-category quality-lane mean is the lead QA number. Across three runs it
ranged from 83.00% to 84.00%; the core Categories 1-4 range was 87.01% to
87.45%. Category 5 robustness averaged 71.50% and is the accuracy weak spot.
It tests adversarial no-answer, wrong-person, and evidence-scope handling rather
than ordinary answer QA.

Quality-lane answer p95 is 14.630 s. The faster lane gives back about one core
accuracy point and cuts answer p95 to 7.047 s. Those seconds are answer-model
and judge time, separate from sub-20 ms retrieval. These are scoped WizeMe
300-question harness results, not a full-dataset or same-mode provider score.

LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3
measures exact-turn retrieval across tightly clustered sessions. LongMemEval
Any@3 measures answer-cluster retrieval across a larger haystack. Both are
reported without cross-benchmark normalization.

Public artifacts disclose dataset revisions, hashes, scope, metrics, timing
boundaries, hardware class, and cache state. WizeMe implementation
configuration and private diagnostic traces are intentionally withheld.

See [the public methods](comparison/METHODS.md), the aggregate receipts under
`results/runs/wizeme/`, and the permanent Zenodo record:

- [Zenodo DOI 10.5281/zenodo.20970433](https://doi.org/10.5281/zenodo.20970433)
- `comparison/WIZEME_PUBLIC_RESULTS_2026-06-27.md`
- `comparison/WIZEME_LOCOMO_E2E_STABILITY_2026-06-27.md`
- `results/wizeme-public-memory-benchmark-2026-06-27.json`
- `results/wizeme-public-memory-datapackage-2026-06-27.json`
- `results/wizeme-public-memory-benchmark-2026-07-16.json`
- `results/wizeme-public-memory-datapackage-2026-07-16.json`
- `results/wizeme-locomo-e2e-stability-3x300.json`

The separate official LongMemEval QA workflow remains:

```bash
python scripts/run_longmemeval_e2e.py \
  --dataset datasets/cache/longmemeval/longmemeval_s_cleaned.json \
  --retrieval results/runs/wizeme/longmemeval/retrieval-turn.json \
  --hypotheses results/runs/wizeme/longmemeval/hypotheses.jsonl \
  --result results/runs/wizeme/longmemeval/end-to-end-qa.json \
  --answer-model google/gemini-3.1-flash-lite-preview

python scripts/run_longmemeval_official_judge.py \
  --hypotheses results/runs/wizeme/longmemeval/hypotheses.jsonl \
  --result results/runs/wizeme/longmemeval/end-to-end-qa.json \
  --revision 9e0b455f4ef0e2ab8f2e582289761153549043fc
```

The first step requires an answer-model credential; the official judge requires
the credential specified by the pinned evaluator. Without both, the receipt
remains explicitly incomplete. Provider rows remain `not_run` until their
adapters execute under the same dataset revision, answer model, judge, prompt,
retrieval depth, cache state, and hardware disclosure.

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

Rubrics are publication and evidence gates: retrieval quality, multi-evidence
feasibility, latency, provenance, freshness/forgetting, and claim safety. They
are not a live intent-classifier or proofreader layer.

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
