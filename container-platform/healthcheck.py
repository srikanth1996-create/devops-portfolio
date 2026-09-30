"""Minimal HTTP health probe for CI smoke tests.

Usage:
    python healthcheck.py --url http://localhost:8000/health

Exits 0 when the endpoint returns 200, 1 otherwise.
"""
import argparse
import sys
import urllib.request


def check(url: str, timeout: int = 10) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.status == 200
    except Exception as exc:  # noqa: BLE001 - any failure means unhealthy
        print(f"Health check failed: {exc}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    sys.exit(0 if check(args.url) else 1)


if __name__ == "__main__":
    main()
