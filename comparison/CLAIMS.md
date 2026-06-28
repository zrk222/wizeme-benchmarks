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

"Across three complete 300-question WizeMe LoCoMo end-to-end QA runs, the
all-category mean was 0.8367 (83.67%), range 0.8300-0.8400. Core Categories
1-4 averaged 0.8730 (87.30%), range 0.8701-0.8745. Category 5 robustness
averaged 0.7150 (71.50%). Conservative answer p95 was 14.630 s. This is not a
full-dataset or same-mode provider leaderboard claim."

"The faster 300-question lane reached 0.8333 (83.33%) all-category and 0.8615
(86.15%) core accuracy at 7.047 s answer p95. Retrieval latency is reported
separately and remains in milliseconds; answer latency is model generation and
judging time."

"Category 5 is WizeMe's disclosed weak QA slice. It primarily tests adversarial
no-answer, wrong-person, and evidence-scope handling. The roadmap target is
better write-time entity/temporal metadata and evidence ownership without
using benchmark labels at runtime."

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
