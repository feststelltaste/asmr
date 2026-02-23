---
title: "LLM Fine-tuning on Codebase"
stage: assess
category: Agentic AI Tools
description: "Fine-tuning models on internal proprietary code for better context-aware suggestions and code completion specific to your architecture."
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
