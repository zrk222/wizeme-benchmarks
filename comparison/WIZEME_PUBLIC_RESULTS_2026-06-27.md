# WizeMe Public Memory Benchmark Summary

Generated: 2026-06-28T02:39:34.545Z

This public summary reports benchmark outcomes, latency, dataset scope, and reproducibility boundaries. Non-public materials, secrets, and private user data are intentionally withheld.

## Published Evidence

- Zenodo DOI: 10.5281/zenodo.20970433
- Zenodo record: https://zenodo.org/records/20970433
- GitHub benchmark repository: https://github.com/zrk222/wizeme-benchmarks
- LinkedIn methods article: https://www.linkedin.com/pulse/ai-memory-race-has-tiny-team-problem-pinnacle-digital-services-ltd-gkbcc/
- LoCoMo 3-run stability receipt: https://wizeme.app/locomo-e2e-stability-3x300.json

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

| Public Row | Scope | QA accuracy | Runs / range | Official-style mean | Answer p95 | Judge p95 | Note |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| LoCoMo E2E QA dual quality lane, all-category stress score | 3 x 300 questions including adversarial Category 5 | 0.8367 (83.67%) | 3 / 83.00-84.00% | 0.7083 (70.83%) | 14630 ms | 12893 ms | Lead quality-lane number: three-run all-category mean. Category 5 is disclosed separately because it uses adversarial empty-answer labels. |
| LoCoMo E2E QA dual quality lane, core Categories 1-4 | 3 x 231 core questions within matched deterministic 300-question gates | 0.8730 (87.30%) | 3 / 87.01-87.45% | 0.7083 (70.83%) | 14630 ms | 12893 ms | Three-run core diagnostic with the full range disclosed. Parallel candidates plus evidence-only adjudication; quality lane, not the default serving path or a same-mode provider row. |
| LoCoMo dual quality lane, adversarial Category 5 | 3 x 69 adversarial questions within matched deterministic gates | 0.7150 (71.50%) | 3 / 68.12-73.91% | n/a | 14630 ms | 12893 ms | Robustness lane only; not ordinary answer QA. |
| LoCoMo E2E QA all-category stress gate | 300-question WizeMe gate including adversarial Category 5 | 0.8333 (83.33%) | 1 / 83.33-83.33% | 0.7095 (70.95%) | 7047 ms | 13491 ms | Current accepted adaptive gate; +0.66 points over the same-run compact control, +10.00 points over the historical prior gate, and 5.90% lower answer p95 than the matched control. Not a full-dataset or same-mode provider row. |
| LoCoMo E2E QA core Categories 1-4 | 231 core questions within the deterministic 300-question gate | 0.8615 (86.15%) | 1 / 86.15-86.15% | 0.7093 (70.93%) | 7047 ms | 13491 ms | +0.87 points over the same-run compact control and +13.42 points over the historical prior core slice. Category 5 is reported separately; this is not a same-mode provider row. |
| LoCoMo adversarial Category 5 robustness | 69 adversarial questions within the deterministic 300-question gate | 0.7391 (73.91%) | 1 / 73.91-73.91% | 0.7101 (71.01%) | 7047 ms | 13491 ms | Reported separately because Category 5 empty-answer labels do not represent ordinary answer QA. |
| LoCoMo E2E QA matched compact control | Same 300 questions, retrieval receipt, providers, judge, and run window | 0.8267 (82.67%) | 1 / 82.67-82.67% | 0.6968 (69.68%) | 7489 ms | 16889 ms | Matched control for isolating the adaptive answer-policy lift from provider/run variance. |
| LoCoMo E2E QA prior core Categories 1-4 | 231 core questions within the historical prior 300-question gate | 0.7273 (72.73%) | 1 / 72.73-72.73% | 0.6993 (69.93%) | 7524 ms | 1073 ms | Historical prior core slice; not the same-run compact control. |
| LoCoMo E2E QA prior gate | 300-question WizeMe end-to-end QA harness gate | 0.7333 (73.33%) | 1 / 73.33-73.33% | 0.7052 (70.52%) | 7524 ms | 1073 ms | Prior E2E QA gate used for the accepted-gate lift comparison. |

## Known Limitations

Lead with the 83.67% all-category three-run mean. Category 5 robustness is the accuracy weak spot at a 71.50% mean and primarily tests adversarial no-answer, wrong-person, and evidence-scope handling. Quality-lane answer p95 is 14.630 s; the faster adaptive lane is 7.047 s. These are model-generation and judging latencies, separate from sub-20 ms retrieval.

## Protocol Boundary

LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 measures exact-turn retrieval across tightly clustered sessions. LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. Both are reported without cross-benchmark normalization.

LoCoMo end-to-end QA accuracy measures judged answers produced from retrieved evidence. The dual quality lane reports a three-run mean and range; the adaptive default and matched control are single complete runs. Core Categories 1-4 and adversarial Category 5 are separate because Category 5 uses empty-answer robustness labels. No slice is comparable to a provider row unless the dataset revision, included categories, answer model, judge, prompt, retrieval depth, cache state, hardware, and raw artifacts are matched.

## Comparison Boundary

Provider rows are sourced public figures or third-party documentation unless explicitly marked same-mode. Direct comparison requires matched dataset revision, task, metric, answer model, judge, k, cache state, hardware, and raw artifacts.

## IP Boundary

- Public docs disclose results and reproducibility boundaries.
- Additional non-public review materials are handled only through controlled diligence.
- No public artifact should expose non-public materials, secrets, or private user data.
