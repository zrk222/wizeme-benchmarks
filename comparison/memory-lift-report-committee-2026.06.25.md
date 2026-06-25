<!-- BEGIN MACHINE RECEIPT -->
{
  "report": {
    "generated_at": "2026-06-25T18:54:12.522Z",
    "protocol_version": "2026.06.25",
    "audience": "committee",
    "status": "positive_lift_below_10pct_target",
    "dataset_integrity": {
      "locomo": {
        "id": "locomo10",
        "raw_sha256": "79FA87E90F04081343B8C8DEBECB80A9A6842B76A7AA537DC9FDF651EA698FF4",
        "expected_sha256": "79FA87E90F04081343B8C8DEBECB80A9A6842B76A7AA537DC9FDF651EA698FF4",
        "sha256_matches_expected": true,
        "manifest_hash": "073D50213F146BDEBDF880ED269DD67AAE5D545E2C7AA3BA2EFCDBB5D82BBB74"
      },
      "longmemeval": {
        "id": "longmemeval_s_cleaned",
        "raw_sha256": "D6F21EA9D60A0D56F34A05B609C79C88A451D2AE03597821EA3D5A9678C3A442",
        "expected_sha256": "D6F21EA9D60A0D56F34A05B609C79C88A451D2AE03597821EA3D5A9678C3A442",
        "sha256_matches_expected": true,
        "manifest_hash": "E831A5E5D8EC9B25E9D09A7FA8DB191740EE43767ADB4C6006D0CF82C4409AD8"
      }
    },
    "stability": {
      "method": "3x timed runs per profile; p95 over three loader passes is the max sample",
      "locomo_accuracy_runs": {
        "cold": 3,
        "warm": 3
      },
      "locomo_fast_runs": {
        "cold": 3,
        "warm": 3
      },
      "longmemeval_runs": {
        "cold": 3,
        "warm": 3
      },
      "loader_seed": "memory-benchmark-lift-loader-v1",
      "loader_wall_clock_ms": {
        "locomo": [
          29.225,
          22.365,
          26.665
        ],
        "longmemeval": [
          3314.744,
          3921.768,
          4641.307
        ]
      }
    },
    "datasets": {
      "locomo": {
        "dialogues": 10,
        "sessions": 272,
        "turns": 5882,
        "evaluated_questions": 1982,
        "protocol": "LoCoMo Any@3 measures exact-turn retrieval across tightly clustered dialogue sessions."
      },
      "longmemeval": {
        "evaluated_questions": 470,
        "unique_haystack_sessions": 19195,
        "summed_per_question_haystack_sessions": 23867,
        "protocol": "LongMemEval Any@3 measures answer-cluster/session retrieval over a larger haystack slice."
      }
    },
    "profiles": {
      "locomo_accuracy": {
        "any3": 0.7124,
        "any3_percent": 71.24,
        "all3": 0.607,
        "all50": 0.8042,
        "cold_p95_ms": 422.52,
        "warm_p95_ms": 17.159,
        "relative_any3_lift_percent": 7.53
      },
      "locomo_fast": {
        "any3": 0.7079,
        "any3_percent": 70.79,
        "all3": 0.6044,
        "all50": 0.8042,
        "cold_p95_ms": 455.423,
        "warm_p95_ms": 8.625
      },
      "locomo_probe": {
        "any3": 0.7367,
        "all3": 0.6633,
        "warm_p95_ms": 15.595
      },
      "longmemeval": {
        "any3": 0.9255,
        "any3_percent": 92.55,
        "raw_turn_all3": 0.0362,
        "cold_p95_ms": 13.094,
        "warm_p95_ms": 11.005
      }
    },
    "ceilings": {
      "locomo": {
        "all50": 0.8042
      },
      "longmemeval": {
        "raw_turn_all3_ceiling": 0.0511,
        "answer_cluster_all3_ceiling": 0.9319
      }
    },
    "benchmark_protocol_disclosure": "LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. Both are reported raw without cross-benchmark normalization.",
    "claim_boundary": "Publish as an updated public retrieval gate with raw artifacts, pinned dataset revision, hardware/runtime metadata, percentages for novice readers, and cold/warm latency disclosed. Do not market it as end-to-end QA, medical advice, public SOTA, or same-mode provider superiority."
  }
}
<!-- END MACHINE RECEIPT -->

## Memory Route Portfolio - Review Committee Summary

- The machine receipt above is the source of truth for due diligence, CI validation, and reproducibility checks.
- Public copy must preserve the benchmark protocol disclosure, raw artifact paths, and safety boundaries.

# Memory Benchmark Lift Receipt

Generated: 2026-06-25T18:54:12.522Z

Status: **positive_lift_below_10pct_target**

## LoCoMo Accuracy Full 3x/3x Gate

| Metric | Baseline full gate | Candidate full 3x/3x gate | Delta | Relative |
|---|---:|---:|---:|---:|
| Recall Any@3 | 0.6625 | 0.7124 | 0.0499 | 7.53% |
| Recall All@3 | 0.5666 | 0.607 | 0.0404 | 7.13% |
| Recall All@50 | 0.7921 | 0.8042 | 0.0121 | 1.53% |
| Cold p95 ms | 244.955 | 422.52 | 177.565 | 72.49% |
| Warm p95 ms | 7.52 | 17.159 | 9.639 | 128.18% |

Novice read: LoCoMo Recall Any@3 0.7124 = 71.24%; Recall All@3 0.607 = 60.7%; Recall All@50 0.8042 = 80.42%.

Benchmark protocol disclosure: LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. Both are reported raw without cross-benchmark normalization.

## LoCoMo Fast Full 3x/3x Gate

| Metric | Baseline full gate | Fast candidate full 3x/3x gate | Delta | Relative |
|---|---:|---:|---:|---:|
| Recall Any@3 | 0.6625 | 0.7079 | 0.0454 | 6.85% |
| Recall All@3 | 0.5666 | 0.6044 | 0.0378 | 6.67% |
| Recall All@50 | 0.7921 | 0.8042 | 0.0121 | 1.53% |
| Cold p95 ms | 244.955 | 455.423 | 210.468 | 85.92% |
| Warm p95 ms | 7.52 | 8.625 | 1.105 | 14.69% |

Fast route note: Fast candidate disables deterministic signature rerank. It preserves most of the full-dataset accuracy lift while materially lowering warm p95 versus the accuracy route; publish only with the accuracy trade-off and higher cold p95 disclosed.

## LoCoMo 300-Query Probe

| Metric | Prior auto probe | Candidate auto probe | Delta | Relative |
|---|---:|---:|---:|---:|
| Recall Any@3 | 0.73 | 0.7367 | 0.0067 | 0.92% |
| Recall All@3 | 0.6567 | 0.6633 | 0.0066 | 1.01% |
| Warm p95 ms | 16.317 | 15.595 | -0.722 | -4.42% |

## LongMemEval Guard

- Any@3: 0.9255 (92.55%)
- Raw-turn All@3: 0.0362 (3.62%)
- Raw-turn All@3 ceiling: 0.0511 (5.11%)
- Answer-cluster/session All@3 ceiling: 0.9319 (93.19%)
- Cold p95 ms: 13.094
- Warm p95 ms: 11.005

## Reproducibility, Generalization, And Scale

- Stability: LoCoMo accuracy and fast routes plus LongMemEval guard are full three-cold plus three-warm timed retrieval gates. They are not averaged across five random seeds; do not claim seed-level variance is solved.
- Generalization: the lift is validated on LoCoMo dialog-turn retrieval, and the long-memory guard remains above target on LongMemEval at 0.9255 (92.55%).
- Benchmark protocol: LoCoMo and LongMemEval use different evaluation protocols. LoCoMo Any@3 measures exact-turn retrieval across 272 tightly clustered sessions. LongMemEval Any@3 measures answer-cluster retrieval across a larger haystack. Both are reported raw without cross-benchmark normalization.
- LoCoMo scale: 10 dialogues, 272 sessions, 5882 turns, 1982 evaluated questions.
- LongMemEval scale: 470 evaluated questions, 19195 unique haystack sessions, 23867 summed per-question haystack sessions.

## Runtime Loader Freshness

- Deterministic loader seed: `memory-benchmark-lift-loader-v1`.
- LoCoMo dataset SHA match: yes; manifest SHA: `073D50213F146BDEBDF880ED269DD67AAE5D545E2C7AA3BA2EFCDBB5D82BBB74`; loader passes ms: 29.225, 22.365, 26.665; loader p95 ms: 29.225.
- LongMemEval dataset SHA match: yes; manifest SHA: `E831A5E5D8EC9B25E9D09A7FA8DB191740EE43767ADB4C6006D0CF82C4409AD8`; loader passes ms: 3314.744, 3921.768, 4641.307; loader p95 ms: 4641.307.
- Loader p95 disclosure: p95 over three deterministic loader passes is the max sample; retrieval p95 is still taken from the full benchmark artifacts.

## Safety Boundaries

- HIPAA/GDPR: write-time entity canonicalization, graph Laplacian features, and spectral indices must remain user/patient isolated unless a differential-privacy layer is explicitly approved and tested.
- Hallucination risk: retrieval confidence gates must abstain when the Bayesian posterior or evidence receipt quality falls below threshold; the partner should say it cannot find the fact in the loaded record instead of inventing it.
- Liability: causal-axis outputs must label edge weights as correlation, user-stated causation, or externally established causation; never imply medical or iatrogenic advice from memory correlations.

## Claim Boundary

Publish as an updated public retrieval gate with raw artifacts, pinned dataset revision, hardware/runtime metadata, percentages for novice readers, and cold/warm latency disclosed. Do not market it as end-to-end QA, medical advice, public SOTA, or same-mode provider superiority.
