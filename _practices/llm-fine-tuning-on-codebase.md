---
title: "LLM Fine-tuning on Codebase"
stage: assess
category: AI Tooling Setup
description: "Fine-tuning models on internal proprietary code for better context-aware suggestions and code completion specific to your architecture."
strategic_value: supporting
devops_phases: [build, operate]
---

## Overview

Fine-tuning adapts a base LLM to your organization's specific coding conventions, internal libraries, and domain patterns. It can make suggestions more relevant than generic models — but has significant cost and complexity.

## Approaches

- **Full fine-tuning** — Expensive; requires significant GPU resources
- **LoRA / QLoRA** — Parameter-efficient fine-tuning; more practical
- **Continued pre-training on code** — Long-horizon training on proprietary code
- **RAG as alternative** — Often achieves similar results with less overhead

## When to Assess

- Your codebase uses heavy internal abstractions that generic models don't understand
- You have the MLOps maturity to manage training pipelines and model versioning
- RAG alone isn't providing sufficient code context

## Risks & Considerations

- Training data must be clean and representative — garbage in, garbage out
- Risk of overfitting to old patterns in legacy code
- Requires ongoing maintenance as the codebase evolves
- Consider RAG first — it is usually simpler and more up-to-date

## Resources

- [Hugging Face — fine-tuning guide](https://huggingface.co/docs/transformers/training) — practical tutorials for LLM fine-tuning
- [LoRA: Low-Rank Adaptation paper](https://arxiv.org/abs/2106.09685) — the technique behind parameter-efficient fine-tuning
- [Axolotl — fine-tuning framework](https://github.com/OpenAccess-AI-Collective/axolotl) — popular open-source fine-tuning tool
- [YouTube — LLM fine-tuning on code explained](https://www.youtube.com/results?search_query=llm+fine+tuning+code+codebase+2025)
