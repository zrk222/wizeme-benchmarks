# WizeMe Public Memory Retrieval Results

Generated from pinned WizeMe public retrieval receipts on June 24, 2026.

## Results

| Dataset | Queries | Recall Any@1 | Recall Any@3 | Recall All@5 | nDCG@5 | Cold p95 | Warm p95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LoCoMo dialog turns | 1,982 | 0.4228 | 0.6625 | 0.6493 | 0.6401 | 196.453 ms | 5.942 ms |
| LongMemEval-S turns | 470 | 0.8426 | 0.9255 | 0.0532 | 0.7071 | 9.576 ms | 9.195 ms |

LongMemEval excludes 30 abstention questions, matching its official retrieval
protocol. LoCoMo excludes questions without annotated dialog evidence.

## Tuning Decisions

- A pinned benchmark-neutral MiniLM cross-encoder reranking the top eight hybrid
  candidates plus safe session-dense evidence buffering lifted full LoCoMo
  Recall Any@3 from 0.4849 to 0.6625 and Recall All@3 from 0.4157 to 0.5666.
- A bounded model-revision-keyed pair cache plus evidence buffering reduced
  learned LoCoMo warm p95 to 5.942 ms. Genuinely cold inference remains
  disclosed at 196.453 ms p95.
- LongMemEval ranks compact sessions before localizing turns and expands around
  ranked anchors with adaptive dense evidence packing. Recall Any@3 remains
  above target at 0.9255.
- LongMemEval reports feasibility ceilings for small-k all-evidence cases:
  overall All@3 is 0.0170, conditional All@3 among possible cases is 0.3333,
  and the All@3 ceiling is only 0.0511 because most questions have more than
  three labeled evidence turns.
- Bayesian evidence support and harmonic agreement combine independent lexical
  and semantic ranks without allowing one score scale to dominate.
- Rubrics now gate evidence sufficiency, multi-evidence feasibility, latency,
  provenance, freshness/forgetting, and claim safety; they do not replace the
  primary LLM as the live intent decider.

## Honest Weaknesses

- LoCoMo dialog-turn localization is materially improved but remains below the
  0.92 target. The next credible lift is a faster distilled relevance model,
  not more handcrafted synonyms.
- LongMemEval Recall Any@3 clears the 0.92 target, but Recall All remains low at
  small k because answer sessions contain many labeled evidence turns.
- These are retrieval metrics. End-to-end QA must use a separately pinned
  answer model and official answer evaluator.
