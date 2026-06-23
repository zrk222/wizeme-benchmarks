# WizeMe Public Memory Retrieval Results

Generated from WizeMe commit `3c8c8f82` on June 23, 2026.

## Results

| Dataset | Queries | Recall Any@1 | Recall Any@3 | Recall All@5 | nDCG@5 | Cold p95 | Warm p95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LoCoMo dialog turns | 1,982 | 0.3330 | 0.5116 | 0.5055 | 0.4970 | 52.878 ms | 27.574 ms |
| LongMemEval-S turns | 470 | 0.8319 | 0.9064 | 0.0362 | 0.7009 | 29.722 ms | 32.989 ms |

LongMemEval excludes 30 abstention questions, matching its official retrieval
protocol. LoCoMo excludes questions without annotated dialog evidence.

## Tuning Decisions

- WizeMe reranking improved a 100-query LoCoMo slice from 0.4000 to 0.4600
  Recall Any@3, but doubled p95 and slightly reduced LongMemEval accuracy.
- Local BGE-small plus BM25 reciprocal-rank fusion reached 0.5600 on that
  LoCoMo slice and generalized to 0.5700 on a disjoint 300-query slice.
- BGE-base did not improve Recall Any@3 and was not selected.
- Session propagation did not improve held-out Recall Any@3 and was rejected.
- The final LoCoMo profile uses pinned BGE-small with vector weight 0.56 and
  lexical weight 0.44.
- The final LongMemEval profile uses the lower-latency BM25 rail.

## Honest Weaknesses

- LoCoMo dialog-turn localization remains moderate. The next credible lift
  requires stronger query-to-evidence semantic training or a benchmark-neutral
  cross-encoder, not more handcrafted synonyms.
- LongMemEval Recall Any@3 is 0.9064, below the 0.92 target by 0.0136.
- Recall All is low on multi-evidence questions. WizeMe often retrieves one
  correct answer turn without retrieving every answer-labeled turn.
- These are retrieval metrics. End-to-end QA must use a separately pinned
  answer model and official answer evaluator.

