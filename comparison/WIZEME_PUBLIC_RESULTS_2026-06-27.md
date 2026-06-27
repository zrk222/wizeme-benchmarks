# WizeMe Public Memory Benchmark Summary

Generated: 2026-06-27T17:16:51.020Z

This public summary reports benchmark outcomes, latency, dataset scope, and reproducibility boundaries. Non-public materials, secrets, and private user data are intentionally withheld.

## Retrieval Metrics

| Public Row | Scope | Any@3 | All@3 | Any@15 | All@15 | Any@50 | All@50 | Cold/Warm p95 | Note |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| LongMemEval full gate | 470-question retrieval gate | 0.9319 (93.19%) | 0.0149 (1.49%) | n/a | 0.5660 (56.60%) | n/a | 0.8489 (84.89%) | 11.827/13.382 ms | Benchmark-specific retrieval metric; not cross-normalized with LoCoMo. |
| LoCoMo full accuracy gate | 1,982-question retrieval gate | 0.7124 (71.24%) | 0.6070 (60.70%) | n/a | n/a | n/a | 0.8042 (80.42%) | 422.52/17.159 ms | Full-dataset dialog-turn retrieval gate. |
| LoCoMo full low-latency gate | 1,982-question retrieval gate with latency optimization enabled | 0.7109 (71.09%) | 0.6049 (60.49%) | 0.8643 (86.43%) | 0.7689 (76.89%) | 0.9026 (90.26%) | 0.8042 (80.42%) | 18.777/20.107 ms | Low-latency public row; not promoted as the accuracy headline because top-3 accuracy is slightly lower. |
| LoCoMo 300-query stability gate | 300-query stability gate with repeated timing | 0.7300 (73.00%) | 0.6533 (65.33%) | 0.8933 (89.33%) | 0.8000 (80.00%) | 0.9400 (94.00%) | 0.8400 (84.00%) | 12.154/9.614 ms | Current-code rerun of the higher 300-query gate; not a full-dataset replacement row. |
| LoCoMo 300-query tuning gate | 300-query tuning gate | 0.7400 (74.00%) | 0.6633 (66.33%) | 0.8933 (89.33%) | 0.8033 (80.33%) | 0.9433 (94.33%) | 0.8500 (85.00%) | 479.58/19.645 ms | Best validated 300-query tuning result; not a full-dataset replacement row. |
| LoCoMo 300-query tail-recall gate | 300-query tuning gate focused on high-k recall | 0.7400 (74.00%) | 0.6633 (66.33%) | 0.8967 (89.67%) | 0.8067 (80.67%) | 0.9500 (95.00%) | 0.8633 (86.33%) | 549.684/28.72 ms | Tail-recall result; non-public materials withheld. |

## End-to-End QA

| Public Row | Scope | QA accuracy | Official-style mean | Answer p95 | Judge p95 | Note |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| LoCoMo E2E QA accepted gate | 300-question WizeMe end-to-end QA harness gate | 0.7933 (79.33%) | 0.7147 (71.47%) | 7232 ms | 1070 ms | Current accepted E2E QA tuning gate; +6.00 points over the prior gate. Not a full-dataset or same-mode provider leaderboard row. |
| LoCoMo E2E QA prior gate | 300-question WizeMe end-to-end QA harness gate | 0.7333 (73.33%) | 0.7052 (70.52%) | 7524 ms | 1073 ms | Prior E2E QA gate used for the accepted-gate lift comparison. |

## Protocol Boundary

LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 measures exact-turn retrieval across tightly clustered sessions. LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. Both are reported raw without cross-benchmark normalization.

LoCoMo end-to-end QA accuracy measures judged answers produced from retrieved evidence. It is separate from retrieval Recall Any@3 and from published provider rows unless the dataset revision, answer model, judge, prompt, retrieval depth, cache state, hardware, and raw artifacts are matched.

## Comparison Boundary

Provider rows are sourced public figures or third-party documentation unless explicitly marked same-mode. Direct comparison requires matched dataset revision, task, metric, answer model, judge, k, cache state, hardware, and raw artifacts.

## IP Boundary

- Public docs disclose results and reproducibility boundaries.
- Additional non-public review materials are handled only through controlled diligence.
- No public artifact should expose non-public materials, secrets, or private user data.
