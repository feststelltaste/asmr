---
title: "Self-hosted Open LLMs"
stage: trial
category: AI Tooling Setup
description: "Running Llama, Mistral, Qwen locally for privacy-sensitive code and data. Viable for many tasks, gap to frontier models still matters for complex reasoning."
strategic_value: generic
devops_phases: [build, operate]
---

# Self-hosted Open LLMs

## Problem

How do you utilize powerful LLMs for modernization tasks on highly sensitive, proprietary, or air-gapped codebases where data residency and privacy requirements prohibit the use of third-party, cloud-based AI providers?

*This problem is difficult because:*

- Frontier models (like GPT-5.2, Claude Sonnet 4.6) are only available via third-party APIs, which often require sending your code to a cloud provider's servers for processing.
- Organizations in highly regulated industries (finance, healthcare, government, defense) often have strict "no-cloud" or "no-data-sharing" policies for their core intellectual property (the source code).
- Self-hosting a large model (e.g., 70B+ parameters) requires significant GPU infrastructure, specialized MLOps expertise, and ongoing operational maintenance.
- There is traditionally a "quality gap" between the best open-weight models and the best closed-source frontier models for complex architectural reasoning and long-context tasks.
- Security: downloading and running unverified model weights can introduce malicious code or "backdoors" into an internal environment.

*Yet, solving this problem is feasible because:*

- The performance gap between open-weight models (Mistral's Devstral, Qwen, DeepSeek) and frontier models has narrowed dramatically in 2024–2025.
- Efficient inference servers (vLLM, Ollama, Hugging Face TGI) and "quantization" techniques allow high-performance models to run on more modest, on-premise hardware.
- Self-hosting gives an organization total control over its data, model versions, and "fine-tuning" pipeline, ensuring 100% data residency and privacy compliance.
- Open models can be "fine-tuned" on internal data more easily and cheaply than closed-source models, allowing them to specialize in a specific legacy domain.

## Solution

Deploy and manage open-weight LLMs within your own secure infrastructure to power modernization agents:

1. **Select an Open-Weight Model** — Choose a model based on your specific task (e.g., **Qwen 3 series** for general reasoning, or **DeepSeek-Coder** for specialized code generation).
2. **Provision the GPU Infrastructure** — Set up internal GPU servers (e.g., NVIDIA H100s or A100s) to host the model. Use **quantization** (4-bit or 8-bit) to reduce the VRAM requirements if needed.
3. **Deploy an Inference Server** — Use **vLLM** (production-grade) or **Ollama** (for local development) to serve the model via an OpenAI-compatible API.
4. **Implement an AI Gateway** — Use an **AI Gateway / Routing** layer (like LiteLLM) to provide a unified interface for your agents, allowing them to switch between local and (if allowed) cloud models seamlessly.
5. **Establish a "Model Vetting" Process** — Only download weights from trusted sources (like Hugging Face's official model cards) and scan them for potential security risks before deployment.
6. **Perform Targeted Fine-tuning** — Use your proprietary legacy code to perform a parameter-efficient fine-tune (**LoRA**) to improve the model's accuracy on your specific domain (see **LLM Fine-tuning on Codebase**).

## Tradeoffs

**Pros:**

- Ensures 100% data residency and privacy, meeting the strictest regulatory and security requirements.
- Zero per-token API costs: the only ongoing costs are for the GPU infrastructure and electricity.
- Total control over model versions: the model won't "change" or be deprecated without your approval.

**Cons:**

- High upfront cost and operational complexity for GPU hardware and MLOps expertise.
- Open models still lag slightly behind the very best frontier models for the most complex, multi-step architectural reasoning.
- You are responsible for model updates, security patching, and "jailbreak" prevention.

**Difficulties:**

- Scaling the inference infrastructure to handle dozens of parallel agentic modernization sessions without significant latency.
- Maintaining the "long-context" performance of open models, which is often lower than specialized frontier models like Gemini 1.5 Pro.

## Rationale

For organizations with high security requirements, cloud-based AI is often a "non-starter." Self-hosted open models bridge this gap, providing "frontier-class" intelligence within the safety of an organization's own firewall. While the operational cost is higher, the value of being able to apply AI to the most sensitive core legacy systems—without compromising security or intellectual property—is transformative for a modernization program.

## Known Uses

- [Llama 3 (Meta)](https://ai.meta.com/llama/) — the most widely used open-weight frontier model, highly capable for general reasoning and code.
- [DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) — a specialized open model for coding tasks that rivals the best closed-source models on many benchmarks.
- [vLLM](https://docs.vllm.ai/) — a high-performance inference engine for serving open-weight models in production.

## References

- [Hugging Face — Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — the industry-standard benchmark for comparing the quality of open-weight models.
- [Ollama](https://ollama.com/) — a popular tool for running open models locally on a developer's machine.

## Related Patterns

- [AI Gateway / Routing](../ai-gateway-routing/) — the gateway provides the unified interface that connects agents to the self-hosted model.
- [LLM Fine-tuning on Codebase](../llm-fine-tuning-on-codebase/) — open models are the primary target for internal fine-tuning projects.
- [Small Language Models (SLMs)](../small-language-models/) — smaller open models are often self-hosted for high-volume, low-complexity tasks.

## What Next

After successfully self-hosting your first general-purpose model, begin experimenting with [LLM Fine-tuning on Codebase](../llm-fine-tuning-on-codebase/) to improve its accuracy on your specific internal APIs and domain patterns.

## Staging History

**Trial (Feb 2026):** Self-hosting open-weight LLMs is currently being trialed by organizations with high security and privacy requirements. While the technology is maturing rapidly, the high operational cost and GPU infrastructure requirements mean it is still an emerging practice for most modernization teams.
