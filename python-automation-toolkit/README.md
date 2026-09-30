# Python Automation Toolkit

## What I built

**8–10 Python utilities** that automated repetitive operational work: log analysis,
environment provisioning checklists, and weekly status reporting.

## Impact

- Roughly **10–15 hours of manual work saved per week**
- Faster incident triage — error summaries in minutes instead of an hour of grepping
- Consistent, repeatable reports for the team

## Demo code

- `log_analyzer.py` — parses application log files and summarizes errors by type and frequency
- `weekly_report.py` — aggregates deployment counts from a CSV export into a Markdown summary
- `sample_data/` — sample log and CSV files so both scripts run as-is

Try them:

```bash
python log_analyzer.py sample_data/app.log
python weekly_report.py sample_data/deploys.csv
```

> Generic recreations for illustration. They run on the included sample data.
