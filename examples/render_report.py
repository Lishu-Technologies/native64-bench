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
        parser.error("两组吞吐必须是有限的正数")

    gain = candidate_rate / baseline_rate - 1
    print(f"# {data['model']} 推理对照\n")
    print(f"{data['gpu']}，{data['parallel_requests']} 路并行，"
          f"每路 {data['prefix_tokens_per_request']:,} token 前缀。"
          f"指标为{data['measure']}。\n")
    print("| 运行路径 | 合计 token/s |")
    print("|---|---:|")
    print(f"| {candidate['label']} | {candidate_rate:.2f} |")
    print(f"| {baseline['label']} | {baseline_rate:.2f} |")
    print(f"\n相对对照吞吐变化为 **{gain:+.2%}**。")
    print("\n报告根据输入的汇总结果生成。")


if __name__ == "__main__":
    main()
