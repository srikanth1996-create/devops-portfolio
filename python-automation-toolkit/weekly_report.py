"""Build a Markdown status summary from a CSV export of deployments.

Usage:
    python weekly_report.py sample_data/deploys.csv

Expected CSV columns: service,environment,status,duration_minutes,date
"""
import csv
import sys
from collections import Counter


def build_report(path: str) -> str:
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    by_status = Counter(r["status"] for r in rows)
    by_env = Counter(r["environment"] for r in rows)
    durations = [int(r["duration_minutes"]) for r in rows if r["duration_minutes"].isdigit()]
    avg_duration = sum(durations) / len(durations) if durations else 0

    lines = [
        "# Weekly Deployment Summary",
        "",
        f"- Total deployments: {len(rows)}",
        f"- Successful: {by_status.get('success', 0)} | Failed: {by_status.get('failed', 0)}",
        f"- By environment: {dict(by_env)}",
        f"- Average duration: {avg_duration:.1f} minutes",
        "",
        "## Per-service counts",
    ]
    for service, count in Counter(r["service"] for r in rows).most_common():
        lines.append(f"- {service}: {count}")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python weekly_report.py <csvfile>")
    print(build_report(sys.argv[1]))
