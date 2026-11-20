# Benchmark methodology

Both tests run Qwen3.5-9B text inference on an RTX 3060 12 GB. Each step advances eight concurrent requests. Throughput is reported as total cached decode tokens per second across all eight requests.

| Fixed workload | Native64 (tokens/s) | Baseline (tokens/s) | Timing and aggregation |
|---|---:|---:|---|
| 4,096 tokens per request, mixed precision | 264.98 | 157.02 | 64 decode steps. The llama.cpp Q4_K_M baseline ran once before and once after the Native64 run. The faster baseline result is reported. |
| 1,024 tokens per request, 8-bit path | 206.59 | 152.79 | 40 decode steps per run. Each path reports the median of two runs. The llama.cpp Q8_0 baseline ran with CUDA Graph enabled. |

Each row uses its corresponding runtime and quantization configuration. The first row measures the Native64 batched execution path. The second measures the Native64 integration with llama.cpp CUDA. Timing begins after context prefill. Deployment benefits can be evaluated separately on the target hardware and production workload.

[Back to the project overview](../README.md) · [Report example](../examples/README.md)
