# Benchmark methodology

## Qwen3.5-9B cached decoding

Both tests run Qwen3.5-9B text inference on an RTX 3060 12 GB. Each step advances eight concurrent requests. Throughput is reported as total cached decode tokens per second across all eight requests.

| Fixed workload | Native64 (tokens/s) | Baseline (tokens/s) | Timing and aggregation |
|---|---:|---:|---|
| 4,096 tokens per request, mixed precision | 264.98 | 157.02 | 64 decode steps. The llama.cpp Q4_K_M baseline ran once before and once after the Native64 run. The faster baseline result is reported. |
| 1,024 tokens per request, 8-bit path | 206.59 | 152.79 | 40 decode steps per run. Each path reports the median of two runs. The llama.cpp Q8_0 baseline ran with CUDA Graph enabled. |

Each row uses its corresponding runtime and quantization configuration. The first row measures the Native64 batched execution path. The second measures the Native64 integration with llama.cpp CUDA. Timing begins after context prefill. Deployment benefits can be evaluated separately on the target hardware and production workload.

## Task quality

### Whisper-small transcription

The evaluation used 128 English clips from eight held-out LibriSpeech dev-clean speakers. Half the clips were under 10 seconds and half were 10 seconds or longer. Native64 and the original FP16 model used the same audio preprocessing, greedy cached decoding, and reference-text normalization.

Across 3,395 reference words, Native64 made 134 word errors (3.947% WER) and FP16 made 138 (4.065%). Lower WER is better. The observed difference was −0.118 percentage points. The paired 95% interval by speaker ranged from −0.509 to +0.211 percentage points, so the sample is consistent with either a small gain or a small loss.

### CLIP ViT-B/32 retrieval

The evaluation used two fixed galleries from COCO train2017. Each gallery contained 512 images and five captions per image. Each query searched only its own gallery. For image-to-text retrieval, a hit means the top-ranked caption belongs to the query image. For text-to-image retrieval, a hit means the top-ranked image matches the query caption.

| Direction | Native64 hits / queries | Xenova Q4F16 hits / queries |
|---|---:|---:|
| Image → text | 814 / 1,024 | 794 / 1,024 |
| Text → image | 3,107 / 5,120 | 3,033 / 5,120 |

Recall@1 is the hit count divided by the query count across both galleries. Differences in percentage points use the unrounded counts. The Native64 model file was 191.49 MiB. The Xenova Q4F16 model files totaled 119.97 MiB and ran with ONNX Runtime on GPU. [Xenova CLIP model files](https://huggingface.co/Xenova/clip-vit-base-patch32/tree/main/onnx)

[Back to the project overview](../README.md) · [Report example](../examples/README.md)
