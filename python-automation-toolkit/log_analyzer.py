"""Summarize errors in application log files.

Usage:
    python log_analyzer.py sample_data/app.log

Expected log format (one event per line):
    2026-09-30 10:15:02 ERROR db Connection timeout after 30s
    2026-09-30 10:15:03 INFO  api Request completed in 120ms
"""
import re
import sys
from collections import Counter

LOG_PATTERN = re.compile(
    r"^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>INFO|WARN|ERROR)\s+"
    r"(?P<component>\S+)\s+(?P<message>.*)$"
)


def analyze(path: str) -> None:
    levels = Counter()
    errors = Counter()
    total = 0

    with open(path) as fh:
        for line in fh:
            match = LOG_PATTERN.match(line.strip())
            if not match:
                continue
            total += 1
            level = match.group("level")
            levels[level] += 1
            if level == "ERROR":
                # Group by the first few words so similar errors collapse together.
                signature = " ".join(match.group("message").split()[:4])
                errors[signature] += 1

    print(f"Lines parsed : {total}")
    print(f"By level     : {dict(levels)}")
    print("\nTop errors:")
    for signature, count in errors.most_common(10):
        print(f"  {count:5d}x  {signature}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python log_analyzer.py <logfile>")
    analyze(sys.argv[1])
