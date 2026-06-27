# Claim Policy

A comparison is publishable only when dataset, revision, task, evaluation mode,
metric definition, and timing boundary match.

## Allowed Now

"On pinned public retrieval runs, WizeMe reached LoCoMo Recall Any@3 0.7124
(71.24%) with 17.159 ms warm p95 and 422.520 ms cold p95. Its low-latency
full gate reached Recall Any@3 0.7109 (71.09%) with 18.777 ms cold p95 and
20.107 ms warm p95. LongMemEval Recall Any@3 is 0.9319 (93.19%) with
11.827 ms cold p95 and 13.382 ms warm p95. Retrieval results disclose cold
and warm timing separately."

"On a matched 300-question WizeMe LoCoMo end-to-end QA harness gate, answer
accuracy improved from 0.7333 (73.33%) to 0.7933 (79.33%), a 6.00 percentage
point lift. The accepted official-style mean was 0.7147 (71.47%). This is not
a full-dataset or same-mode provider leaderboard claim."

"LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3
measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval
Any@3 measures answer-cluster retrieval across a larger haystack. Both are
reported without cross-benchmark normalization."

"WizeMe uses rubrics as publication and evidence gates for retrieval quality,
multi-evidence feasibility, latency, provenance, freshness/forgetting, and
claim safety. Rubrics are not a live intent-classifier or proofreader layer."

"The same-mode LongMemEval end-to-end QA group remains incomplete until
WizeMe and provider hypotheses are judged with the same pinned official
evaluator."

"WizeMe's synthetic regression suite reached Recall@3 1.0 and FAMA 1.0, with
15.66 ms semantic ANN end-to-end p95 on the recorded local run."

## Blocked Pending Matched Competitor Runs

- "WizeMe is two orders of magnitude faster than elite systems."
- "WizeMe has perfect long-term memory."
- "WizeMe is close to Supermemory."
- "WizeMe beats provider QA benchmarks."
- "93.19% is WizeMe's universal memory accuracy."

These require normalized competitor receipts in the same comparison group.
