---
title: "AI Gateway / Routing"
stage: assess
category: AI Tooling Setup
description: "Routing LLM requests dynamically across models by cost, capability, or latency (LiteLLM, Portkey). Valuable for multi-model setups."
strategic_value: generic
devops_phases: [build, operate]
---

## Overview

An AI gateway sits in front of multiple LLM providers and routes requests based on rules: route cheap/simple tasks to a small model, complex reasoning to a frontier model, fallback on provider outages. It also provides a unified API surface, caching, rate limiting, and cost tracking.

## Tools

- **LiteLLM** — Open-source, supports 100+ models with OpenAI-compatible API
- **Portkey** — Managed gateway with routing, caching, observability
- **Martian** — Semantic routing based on request complexity
- **Braintrust** — AI dev platform with built-in routing and evaluation

## When to Assess

- You use multiple providers and want a single integration point
- Cost optimization: route simpler tasks to cheaper models automatically
- High availability: failover across providers transparently
- You want centralized cost tracking and rate limiting

## Risks & Considerations

- Adds a network hop and potential failure point
- Complex routing logic can be hard to debug
- Provider-specific features may not be accessible through the unified API layer

## Resources

- [LiteLLM documentation](https://docs.litellm.ai/) — open-source gateway supporting 100+ models
- [Portkey](https://portkey.ai/) — managed AI gateway with routing and observability
- [YouTube — LiteLLM setup and usage](https://www.youtube.com/results?search_query=litellm+ai+gateway+routing+2025)
