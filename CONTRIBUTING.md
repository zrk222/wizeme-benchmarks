# Contributing Results

System authors and independent researchers are welcome to submit normalized
results.

1. Pin the dataset revision.
2. Record the exact command, hardware, run count, and warm/cold state.
3. Write a receipt matching `benchmark-result.schema.json`.
4. Place raw receipts under `results/runs/<system>/<dataset>/`.
5. Run:

```bash
python scripts/validate_results.py
python scripts/generate_comparison_report.py
```

Do not copy a number from a blog or leaderboard without its evaluation details.
Third-party published claims may be cataloged, but they cannot enter a direct
comparison group until the task and metric contract match.

