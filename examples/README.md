# 推理对照报告样品

[数据样品](qwen35-9b-b8.json)记录已测的 Qwen3.5-9B 八位对照。脚本使用 Python 3 标准库，从汇总数据生成 Markdown 表。

在仓库根目录运行以下命令。

```bash
python -X utf8 examples/render_report.py
```

预期输出含 Native64 **206.59 token/s**、对照 **152.79 token/s**，以及相对变化 **+35.21%**。将同结构的另一份 JSON 路径作为参数，即可用自己的汇总结果生成报告。

这个样品执行报告生成。实际推理的测试口径见[性能对照说明](../docs/benchmark-method.md)。
