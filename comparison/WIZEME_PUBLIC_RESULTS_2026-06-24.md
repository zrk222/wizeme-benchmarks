# WizeMe Public Memory Retrieval Results

Generated from pinned WizeMe public retrieval receipts refreshed on June 25, 2026.

## Results

| Dataset | Queries | Recall Any@1 | Recall Any@3 | Recall All@5 | nDCG@5 | Cold p95 | Warm p95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LoCoMo dialog turns, accuracy route | 1,982 | 0.4334 | 0.7124 | 0.6736 | 0.6734 | 422.520 ms | 17.159 ms |
| LongMemEval-S turns | 470 | 0.8426 | 0.9255 | 0.0617 | 0.7139 | 13.094 ms | 11.005 ms |

LongMemEval excludes 30 abstention questions, matching its official retrieval
protocol. LoCoMo excludes questions without annotated dialog evidence.

LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3
measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval
Any@3 measures answer-cluster retrieval across a larger haystack. Both are
reported raw without cross-benchmark normalization.

## Tuning Decisions

- Adaptive mesh routing, deterministic signature rerank, and safe evidence
  packing lifted full LoCoMo Recall Any@3 from the prior public full gate
  0.6625 to 0.7124, a 7.53% relative lift. Recall All@3 improved from 0.5666
  to 0.6070.
- The LoCoMo fast route preserves 0.7079 Any@3 while lowering warm p95 to
  8.625 ms. Genuinely cold LoCoMo remains disclosed at 422.520 ms on the
  accuracy route and 455.423 ms on the fast route.
- LongMemEval ranks compact sessions before localizing turns and expands around
  ranked anchors with adaptive dense evidence packing. Recall Any@3 remains
  above target at 0.9255.
- LongMemEval reports feasibility ceilings for small-k all-evidence cases:
  overall All@3 is 0.0362, conditional All@3 among possible cases is 0.7083,
  and the All@3 ceiling is only 0.0511 because most questions have more than
  three labeled evidence turns.
- Bayesian evidence support and harmonic agreement combine independent lexical
  and semantic ranks without allowing one score scale to dominate.
- Rubrics now gate evidence sufficiency, multi-evidence feasibility, latency,
  provenance, freshness/forgetting, and claim safety; they do not replace the
  primary LLM as the live intent decider.

## Honest Weaknesses

- LoCoMo dialog-turn localization is materially improved but remains below the
  0.92 aspiration. The next credible lift is richer write-time temporal/entity
  memory plus a faster distilled relevance model, not more handcrafted synonyms.
- LongMemEval Recall Any@3 clears the 0.92 target, but Recall All remains low at
  small k because answer sessions contain many labeled evidence turns.
- These are retrieval metrics. End-to-end QA must use a separately pinned
  answer model and official answer evaluator.
