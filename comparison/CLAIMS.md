# Claim Policy

A comparison is publishable only when dataset, revision, task, evaluation mode,
metric definition, and timing boundary match.

## Allowed Now

"On pinned public retrieval runs, WizeMe reached LoCoMo Recall Any@3 0.7124
(71.24%) with 17.159 ms warm p95 and 422.520 ms cold p95 on the accuracy
route. The LoCoMo fast route reached Recall Any@3 0.7079 (70.79%) with
8.625 ms warm p95 and 455.423 ms cold p95. LongMemEval-S Recall Any@3 is
0.9255 (92.55%) with 11.005 ms warm p95 and 13.094 ms cold p95. Each result
includes three cold and three warm timed runs."

"LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3
measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval
Any@3 measures answer-cluster retrieval across a larger haystack. Both are
reported raw without cross-benchmark normalization."

"WizeMe uses rubrics as publication and evidence gates for retrieval quality,
multi-evidence feasibility, latency, provenance, freshness/forgetting, and
claim safety. Rubrics are not a live intent-classifier or proofreader layer."

"The same-mode LongMemEval end-to-end QA group is wired, but all rows remain
unpublishable as scores until WizeMe/provider hypotheses and the official
gpt-4o judge artifacts are present."

"WizeMe's synthetic regression suite reached Recall@3 1.0 and FAMA 1.0, with
15.66 ms semantic ANN end-to-end p95 on the recorded local run."

## Blocked Pending Matched Competitor Runs

- "WizeMe is two orders of magnitude faster than elite systems."
- "WizeMe has perfect long-term memory."
- "WizeMe is close to Supermemory."
- "WizeMe beats provider QA benchmarks."
- "92.55% is WizeMe's universal memory accuracy."

These require normalized competitor receipts in the same comparison group.
