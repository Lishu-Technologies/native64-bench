# Inference comparison example

The [sample data](qwen35-9b-b8.json) contain archived Qwen3.5-9B 8-bit results. The script uses the Python 3 standard library to generate a Markdown table from the aggregate results.

Run this command from the repository root.

```bash
python -X utf8 examples/render_report.py
```

The output includes **206.59 tokens/s** for Native64, **152.79 tokens/s** for the baseline, and a relative change of **+35.21%**. Pass another JSON file with the same structure to generate a report from your own aggregate results.

The example generates a report. For the inference test conditions, see [Benchmark methodology](../docs/benchmark-method.md).
