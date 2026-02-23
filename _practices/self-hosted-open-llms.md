---
title: "Self-hosted Open LLMs"
stage: trial
category: AI Tooling Setup
description: "Running Llama, Mistral, Qwen locally for privacy-sensitive code and data. Viable for many tasks, gap to frontier models still matters for complex reasoning."
strategic_value: generic
devops_phases: [build, operate]
---

## Overview

Open-weight models (Llama 3, Mistral, Qwen, DeepSeek) can be self-hosted on GPU infrastructure, eliminating data-sharing with third-party providers. The quality gap to frontier closed-source models has narrowed significantly in 2024–2025.

## When Self-hosting Makes Sense

- Strict data residency or privacy requirements
- High-volume, latency-sensitive inference where API costs are prohibitive
- Fine-tuning on proprietary data
- Air-gapped environments

## Tooling

- **Ollama** — Simple local model management and serving
- **vLLM** — Production-grade inference server with PagedAttention
- **LM Studio** — Developer-friendly local model UI
- **Hugging Face TGI** — Text Generation Inference for production

## Risks & Considerations

- GPU costs and operational complexity are significant
- Frontier tasks (complex reasoning, long-context) still benefit from closed-source models
- Model updates require your own process; you won't automatically get improvements
- Security: downloaded model weights must be verified; malicious weights are a real threat

## Resources

- [Ollama](https://ollama.com/) — simplest way to run open models locally
- [vLLM documentation](https://docs.vllm.ai/) — production-grade open-source inference engine
- [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — compare open model quality
