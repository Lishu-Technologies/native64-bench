"""Render a Markdown comparison from aggregate benchmark results."""

import argparse
import json
from math import isfinite
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "results",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("qwen35-9b-b8.json"),
    )
    args = parser.parse_args()

    data = json.loads(args.results.read_text(encoding="utf-8"))
    candidate = data["candidate"]
    baseline = data["baseline"]
    candidate_rate = float(candidate["tokens_per_second"])
    baseline_rate = float(baseline["tokens_per_second"])
    if any(not isfinite(rate) or rate <= 0 for rate in (candidate_rate, baseline_rate)):
        parser.error("Both throughput values must be finite positive numbers.")

    gain = candidate_rate / baseline_rate - 1
    print(f"# {data['model']} Inference Comparison\n")
    print(
        f"{data['gpu']}, {data['parallel_requests']} concurrent requests, "
        f"{data['prefix_tokens_per_request']:,} prefix tokens per request. "
        f"The metric is {data['measure']}.\n"
    )
    print("| Inference path | Aggregate tokens/s |")
    print("|---|---:|")
    print(f"| {candidate['label']} | {candidate_rate:.2f} |")
    print(f"| {baseline['label']} | {baseline_rate:.2f} |")
    print(f"\nThroughput relative to the baseline changed by **{gain:+.2%}**.")
    print("\nThis report uses the aggregate results supplied in the input file.")


if __name__ == "__main__":
    main()
