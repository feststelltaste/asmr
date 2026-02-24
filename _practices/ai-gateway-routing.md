---
title: "AI Gateway / Routing"
stage: assess
category: AI Tooling Setup
description: "Routing LLM requests dynamically across models by cost, capability, or latency (LiteLLM, Portkey). Valuable for multi-model setups."
strategic_value: generic
devops_phases: [build, operate]
---

# AI Gateway / Routing

## Problem

How do you efficiently manage, route, and optimize LLM requests across multiple providers and models to ensure cost-effectiveness, reliability, and high performance for your modernization agents?

*This problem is difficult because:*

- Different LLM providers (Anthropic, OpenAI, Google) have different strengths, costs, and latency profiles—and these strengths shift as new models are released.
- Modernization tasks range from "simple" code explanation to "complex" multi-file refactoring, each requiring a different level of reasoning capability and cost.
- Relying on a single provider creates a "single point of failure" for your modernization efforts, making you vulnerable to outages or sudden API changes.
- Centralized tracking of API costs, rate limits, and usage patterns across many independent agents is difficult without a unified entry point.

*Yet, solving this problem is feasible because:*

- Specialized AI gateways have emerged that provide a unified, OpenAI-compatible API surface for over 100+ different models.
- "Semantic routing" can automatically analyze the complexity of a request and direct it to the cheapest model that can reliably handle the task.
- Built-in caching and failover mechanisms in these gateways provide immediate reliability improvements for agentic workflows.

## Solution

Implement an AI gateway as the single entry point for all LLM requests from your modernization agents:

1. **Deploy a unified gateway** — Use tools like **LiteLLM** (open-source) or **Portkey** (managed) to create a single, OpenAI-compatible API for all your agents.
2. **Configure model routing rules** — Define rules to route requests based on their nature (e.g., "route all simple code explanations to a small model like Claude 3 Haiku, but route all refactoring tasks to Claude 3.5 Sonnet").
3. **Implement failover and retries** — Configure the gateway to automatically failover to a different provider or model (e.g., from OpenAI to Anthropic) if the primary provider is down or rate-limited.
4. **Enable prompt and response caching** — Use the gateway's built-in caching to save costs and reduce latency for repetitive tasks (like explaining the same legacy function multiple times).
5. **Centralize observability and cost tracking** — Use the gateway to monitor which agents are consuming the most tokens and which models are providing the best "bang for buck" for your specific codebase.

**Key routing strategies:**

- **Cost-based routing** — Prioritize cheaper models for routine, non-critical tasks.
- **Latency-based routing** — Route requests to the fastest model for real-time interactive assistant use.
- **Fallback routing** — Use a backup model if the primary choice fails or hits a rate limit.
- **Semantic routing** — Use an LLM or a classifier to determine the complexity of a task before routing it to the appropriate model.

## Tradeoffs

**Pros:**

- Reduces the "single provider" risk and provides a consistent interface for all agents.
- Dramatically lowers API costs by routing simpler tasks to cheaper models.
- Provides a centralized audit log of all agent activity and costs.

**Cons:**

- Adds a network hop and a potential failure point into the architecture.
- Advanced provider-specific features (like special token formats or specific API parameters) may not be fully supported by the gateway.

**Difficulties:**

- Initial configuration of routing rules and secrets across multiple providers can be complex.
- Debugging "routing drift" where a request is sent to an underpowered model that fails to complete the task.

## Rationale

Modernization agents are token-hungry; they often read thousands of lines of code and generate large refactoring plans. Without a gateway, the cost of running these agents can quickly escalate, and the failure of a single API provider can bring the entire modernization effort to a halt. A gateway provides the "traffic control" layer needed to make agentic workflows sustainable, reliable, and cost-effective at an organizational scale.

## Known Uses

- [LiteLLM](https://docs.litellm.ai/) — the industry-standard open-source gateway for routing LLM requests across 100+ providers.
- [Portkey](https://portkey.ai/) — a popular managed platform for routing, caching, and observability in AI-native applications.
- [Braintrust](https://www.braintrust.dev/) — an AI development platform that includes sophisticated proxy and routing capabilities.

## References

- [Martian — Model Routing](https://withmartian.com/) — one of the first platforms to formalize the concept of "semantic routing" between LLMs based on task complexity.
- [LangChain — LLM Routers](https://python.langchain.com/docs/how_to/routing/) — provides primitives for building simple routing logic directly within an application.

## Related Patterns

- [Agentic Coding Workflows](agentic-coding-workflows.md) — gateways provide the reliable, cost-effective API surface these agents need to operate.
- [LLM Observability & Tracing](llm-observability-and-tracing.md) — gateways are often the primary source of the data used for tracing and debugging agents.
- [Self-hosted Open LLMs](self-hosted-open-llms.md) — gateways can route requests to internal, self-hosted models for sensitive legacy data.

## What Next

After setting up a gateway, implement [LLM Observability & Tracing](llm-observability-and-tracing.md) to begin auditing the cost and quality of your agent's interactions with the different routed models.

## Staging History

**Assess (Feb 2026):** AI gateways are becoming a standard part of the "AI stack." Teams starting with a single model may not need one immediately, but as soon as they begin using multiple providers or scaling their agent usage, a gateway becomes a critical piece of infrastructure.
