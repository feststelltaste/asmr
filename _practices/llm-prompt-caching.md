---
title: "LLM Prompt Caching"
stage: apply
category: AI Tooling Setup
description: "Reusing cached prefix computations on repeated system prompts (Anthropic, OpenAI). Reduces cost and latency for agents with large static contexts."
strategic_value: generic
devops_phases: [build, operate]
---

## Overview

When many API calls share a large common prefix (a system prompt, a codebase context, a set of instructions), prompt caching allows the provider to reuse the KV-cache from that prefix. This saves cost (typically 80–90% on cached tokens) and reduces latency.

## Provider Support

| Provider | Feature Name | Cache Control |
|----------|-------------|---------------|
| Anthropic | Cache control breakpoints | Explicit `cache_control` parameter |
| OpenAI | Automatic prompt caching | Automatic for long prompts |
| Google | Context caching | Explicit API |

## When It Matters

- **Agentic workflows** with a large, stable system prompt
- **RAG pipelines** where the same retrieved docs are used across many calls
- **Code analysis agents** that load an entire file/module as context per call
- Any use case where cost or latency of repeated long prompts is a concern

## Risks & Considerations

- Cache hits are not guaranteed — providers may evict cached content
- Caching benefits are highest when the cached prefix is long (>1K tokens)
- Structure prompts so the stable prefix comes before the dynamic user input

## Resources

- [Anthropic — Prompt caching guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — official documentation with examples
- [OpenAI — Prompt caching](https://platform.openai.com/docs/guides/prompt-caching) — OpenAI's automatic caching behavior
