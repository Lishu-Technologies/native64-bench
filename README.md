# Native64

Native64 helps teams run compressed models on their own hardware. On a single RTX 3060 12 GB serving eight concurrent Qwen3.5-9B requests, Native64 achieved **68.8% higher cached decode throughput** than llama.cpp Q4_K_M at 4,096 tokens of context per request. In a separate 8-bit test at 1,024 tokens per request, the gain was **35.2%** over llama.cpp Q8_0 with CUDA Graph enabled.

## Benchmark highlights

Throughput is the total across all eight requests. Timing starts after prefill and covers steady-state decoding with a fixed batch.

| Qwen3.5-9B configuration | Context per request | Native64 (tokens/s) | llama.cpp baseline (tokens/s) | Gain |
|---|---:|---:|---|---:|
| Mixed precision | 4,096 tokens | 264.98 | 157.02 · Q4_K_M | +68.8% |
| 8-bit inference | 1,024 tokens | 206.59 | 152.79 · Q8_0, CUDA Graph enabled | +35.2% |

[Timing and baseline settings](docs/benchmark-method.md#qwen35-9b-cached-decoding)

## Model coverage

The engineering archive covers Qwen3.5-9B, SmolLM3-3B, OLMoE, Mamba-130M, Whisper-small, CLIP ViT-B/32, VideoMAE Base, and DiT-XL/2-256. The following quality checks measure transcription and image–text retrieval on fixed evaluation samples.

| Model and task | Native64 | Reference | Observed difference |
|---|---:|---|---|
| Whisper-small · English transcription | 3.947% word error rate | 4.065% · original weights, FP16 inference | 4 fewer word errors across 3,395 reference words |
| CLIP ViT-B/32 · image → text retrieval | 79.49% Recall@1 | 77.54% · Xenova Q4F16 | +1.95 percentage points |
| CLIP ViT-B/32 · text → image retrieval | 60.68% Recall@1 | 59.24% · Xenova Q4F16 | +1.45 percentage points |

Whisper used 128 English clips from eight held-out speakers. CLIP used two separate COCO galleries of 512 images each. [Quality evaluation details](docs/benchmark-method.md#task-quality)

## Report example

Generate a Markdown comparison table from the archived 8-bit Qwen results. The script uses the Python standard library.

```bash
python -X utf8 examples/render_report.py
```

[Sample data](examples/qwen35-9b-b8.json) · [Example instructions](examples/README.md)

## Commercial inquiries

For a pilot, hardware porting assessment, or technology licensing, contact **[founder@lishudijun.com](mailto:founder@lishudijun.com)**.

When requesting a pilot, include your model version, target accelerator and memory, current inference backend, and typical workload. We use those details to agree on a task-quality target and compare throughput, latency, and peak device memory on your hardware.
