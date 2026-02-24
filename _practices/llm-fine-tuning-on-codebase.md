---
title: "LLM Fine-tuning on Codebase"
stage: assess
category: AI Tooling Setup
description: "Fine-tuning models on internal proprietary code for better context-aware suggestions and code completion specific to your architecture."
strategic_value: supporting
devops_phases: [build, operate]
---

# LLM Fine-tuning on Codebase

## Problem

How do you improve the accuracy, relevance, and "project-specific" knowledge of an LLM beyond what simple prompting and RAG (Retrieval-Augmented Generation) can provide for a massive, proprietary legacy codebase?

*This problem is difficult because:*

- Large proprietary codebases often use internal libraries, domain-specific languages (DSLs), and unique architectural patterns that are not represented in the LLM's public training data.
- Prompt engineering has "context limits"—you cannot fit your entire 10-million-line codebase and all its architectural conventions into a single system prompt.
- RAG (Retrieval-Augmented Generation) is excellent at finding specific code snippets but struggles to teach the LLM the "global" conventions and "style" of the project.
- Fine-tuning a large model is traditionally expensive, requires a high-quality "clean" dataset, and is difficult to maintain as the code evolves.
- Overfitting is a risk: a model fine-tuned too heavily on legacy patterns might reproduce the very "bad" code you are trying to modernize.

*Yet, solving this problem is feasible because:*

- Parameter-efficient fine-tuning (PEFT) techniques like **LoRA** (Low-Rank Adaptation) and **QLoRA** have dramatically reduced the GPU resources and data needed to fine-tune a model.
- "Continued pre-training" on internal code can teach a model the "vocabulary" and "syntax" of your specific domain and internal APIs without requiring the full cost of training from scratch.
- Fine-tuned models can achieve higher performance on specialized, repetitive tasks (like translating legacy COBOL to modern, idiomatic Java 21) than even the largest frontier models.

## Solution

In highly specialized scenarios, perform a targeted fine-tune of a base LLM to improve its performance on your specific modernization tasks:

1. **Identify the "Specialized Need"** — Fine-tuning is most effective when you have a unique, repetitive task (e.g., "Translating a proprietary 4GL language to TypeScript") or a very large internal API that generic models consistently misunderstand.
2. **Prepare a High-Quality Dataset** — Curate a dataset of "Gold Standard" examples (e.g., "Legacy code before" and "Clean, refactored code after"). This is the most critical and time-consuming step.
3. **Use Parameter-Efficient Fine-Tuning (PEFT)** — Employ techniques like **LoRA** or **QLoRA** to fine-tune a smaller base model (like CodeLlama or Mistral) on your internal data with minimal GPU resources.
4. **Evaluate against a "Golden Set"** — Use **LLM-as-Judge Evaluation** to compare the fine-tuned model's output against the base model's on a representative set of modernization tasks.
5. **Combine with RAG** — Fine-tuning is not a replacement for RAG; use fine-tuning for "global knowledge" (conventions, style, APIs) and RAG for "local context" (specific files, current task).

**When to fine-tune versus RAG:**

- **RAG** — for specific facts, snippets, and current codebase context. (Easier, cheaper, always up-to-date).
- **Fine-tuning** — for style, conventions, internal DSLs, and specialized translation tasks. (Harder, more expensive, static).

## Tradeoffs

**Pros:**

- Dramatically improves the model's ability to follow project-specific conventions and use internal libraries correctly.
- Can reduce the number of tokens needed in the prompt (as the model already "knows" the global context).
- Enables the use of smaller, faster, self-hosted models for tasks that would otherwise require expensive frontier models.

**Cons:**

- High cost in terms of human time (for data curation) and GPU resources (for training).
- Fine-tuned models are "static" and must be re-trained as the codebase or conventions evolve.
- Risk of "regressing" on the model's general reasoning abilities if the fine-tuning is too aggressive.

**Difficulties:**

- Getting a "clean" dataset: legacy codebases are full of inconsistent patterns, and training on them can reinforce the very "debt" you are trying to pay down.
- MLOps maturity: managing model versions, training pipelines, and serving infrastructure is a significant engineering challenge.

## Rationale

Fine-tuning is a "strategic investment" in the model's intelligence. For most modernization tasks, a combination of prompt engineering and RAG is sufficient. However, for organizations with massive, highly unique codebases or proprietary languages, fine-tuning provides the "last 10%" of accuracy and reliability needed to automate the most complex parts of the system. It is the tool that turns a "generic" AI into a "specialized" modernization expert for your specific codebase.

## Known Uses

- [LoRA: Low-Rank Adaptation](https://arxiv.org/abs/2106.09685) — the foundational research paper for parameter-efficient fine-tuning.
- [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) — a popular open-source framework for fine-tuning LLMs with various PEFT techniques.
- [Hugging Face](https://huggingface.co/docs/transformers/training) — the industry-standard platform and library for training and fine-tuning models.

## References

- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) — research on fine-tuning large models on a single consumer-grade GPU.
- [Continued Pre-training of LLMs for Code](https://arxiv.org/abs/2401.04705) — research on adapting models to specific coding domains.

## Related Patterns

- [RAG (Retrieval-Augmented Generation)](../rag-retrieval-augmented-generation/) — fine-tuning and RAG are complementary techniques; use both for maximum effectiveness.
- [LLM-as-judge Evaluation](../llm-as-judge-evaluation/) — essential for measuring the actual improvement (or regression) of a fine-tuned model.
- [Self-hosted Open LLMs](../self-hosted-open-llms/) — fine-tuned models are often self-hosted for security and cost reasons.

## What Next

After establishing a successful RAG pipeline, identify your most repetitive and specialized modernization task and begin curating a small "Gold Standard" dataset to experiment with **LoRA** fine-tuning.

## Staging History

**Assess (Feb 2026):** Fine-tuning on internal code is assessed for specialized modernization tasks where RAG is insufficient. While techniques like LoRA have lowered the barrier to entry, the high cost of data curation and model maintenance means it is currently a specialized practice for large-scale, unique codebases.
