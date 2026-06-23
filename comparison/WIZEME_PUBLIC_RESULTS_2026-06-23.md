# WizeMe Public Memory Retrieval Results

Generated from WizeMe commit `0bc50fd7` on June 23, 2026.

## Results

| Dataset | Queries | Recall Any@1 | Recall Any@3 | Recall All@5 | nDCG@5 | Cold p95 | Warm p95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LoCoMo dialog turns | 1,982 | 0.4945 | 0.6473 | 0.5969 | 0.6202 | 269.005 ms | 177.497 ms |
| LongMemEval-S turns | 470 | 0.8426 | 0.9319 | 0.0191 | 0.5705 | 19.440 ms | 16.816 ms |

LongMemEval excludes 30 abstention questions, matching its official retrieval
protocol. LoCoMo excludes questions without annotated dialog evidence.

## Tuning Decisions

- A pinned MiniLM cross-encoder reranking the top 18 hybrid candidates lifted
  full LoCoMo Recall Any@3 from 0.5116 to 0.6473.
- The cross-encoder is a deep-retrieval lane because its 177.497 ms warm p95 is
  materially slower than the lexical hot path.
- LongMemEval now ranks compact sessions before localizing turns. This lifted
  Recall Any@3 from 0.9064 to 0.9319 while reducing warm p95 to 16.816 ms.
- Multi-evidence expansion begins after the protected top three. It preserved
  Recall Any@3 and lifted Recall All@50 from 0.0750 to 0.4000.
- Bayesian evidence support and harmonic agreement combine independent lexical
  and semantic ranks without allowing one score scale to dominate.

## Honest Weaknesses

- LoCoMo dialog-turn localization remains moderate. The next credible lift
  requires query-to-evidence relevance training beyond the benchmark-neutral
  cross-encoder, not more handcrafted synonyms.
- LongMemEval Recall Any@3 clears the 0.92 target, but Recall All remains low at
  small k because answer sessions contain many labeled evidence turns.
- These are retrieval metrics. End-to-end QA must use a separately pinned
  answer model and official answer evaluator.
