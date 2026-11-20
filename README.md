# Native64

Native64 provides model compression, batched inference optimization, and hardware porting assessments for local and on-premises deployment. It focuses on improving batch throughput on existing hardware and checking output quality for each task.

## Benchmark highlights

Qwen3.5-9B text inference on the same RTX 3060 12 GB. Throughput is the total across eight concurrent requests.

| Native64 path | Concurrent requests | Context per request | Native64 | Baseline | Baseline throughput |
|---|---:|---:|---:|---|---:|
| Mixed precision | 8 | 4,096 tokens | **264.98 tokens/s** | llama.cpp Q4_K_M | 157.02 tokens/s |
| 8-bit inference | 8 | 1,024 tokens | **206.59 tokens/s** | llama.cpp Q8_0 with CUDA Graph enabled | 152.79 tokens/s |

Each row is a separate fixed-batch test. Timing starts after prefill and measures steady-state cached decoding. [Benchmark methodology](docs/benchmark-method.md)

## Model coverage

The engineering archive covers Qwen3.5-9B, SmolLM3-3B, OLMoE, Mamba-130M, Whisper-small, CLIP ViT-B/32, VideoMAE Base, and DiT-XL/2-256. Quality checks use task-specific metrics for text, speech, retrieval, video, and generation. Performance depends on the hardware and workload.

## Report example

The [sample results](examples/qwen35-9b-b8.json) contain an archived 8-bit inference comparison. Run the script to generate a Markdown table and calculate the throughput difference.

```bash
python -X utf8 examples/render_report.py
```

The script renders existing aggregate results. [Example instructions](examples/README.md)

## Commercial inquiries

Native64 is available for batched inference optimization, hardware-specific porting, and technology licensing. For a pilot, share the target accelerator, model version, and current inference backend. Evaluations use the customer's workload to measure task quality, throughput, latency, and peak device memory. Project materials are shared directly for agreed evaluations.
