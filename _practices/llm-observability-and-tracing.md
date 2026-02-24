---
title: "LLM Observability & Tracing"
stage: apply
category: AI Tooling Setup
description: "Langfuse, LangSmith, Arize — tracking LLM calls, costs, latencies, and outputs in production. Necessary as soon as agents touch real workflows."
strategic_value: supporting
devops_phases: [operate, monitor]
---

# LLM Observability & Tracing

## Problem

How do you debug, monitor, and optimize the opaque "thinking process" and tool interactions of multiple AI agents as they execute complex modernization tasks across a massive codebase?

*This problem is difficult because:*

- Agentic workflows are non-deterministic: an agent might take a different path to the same solution every time, making it hard to reproduce and debug failures.
- Each LLM interaction is a "black box"—you only see the prompt and the response, not the model's internal reasoning or the "history" of the conversation.
- Agents use tools (shell, file system, external APIs), and these interactions can have side effects that are difficult to trace back to a specific LLM call.
- Centralized tracking of API costs, token usage, and latency across many independent agents is impossible without a unified "tracing" layer.
- "Hallucinations" and "loops" (where an agent gets stuck in a repetitive action) can go unnoticed for hours without real-time monitoring and alerting.

*Yet, solving this problem is feasible because:*

- Specialized LLM observability platforms have emerged that capture "traces" of every prompt, response, and tool call as a structured event.
- Open standard protocols like **OpenTelemetry** and **OpenLLMetry** allow for the unified collection of traces across different programming languages and LLM providers.
- Real-time visualization of "agentic graphs" (showing the steps an agent took, including its tools) makes it possible to "see inside the brain" of the agent and identify precisely where it went wrong.

## Solution

Implement a centralized observability and tracing platform for all AI agent interactions within your modernization project:

1. **Deploy a Tracing Backend** — Use open-source (e.g., **Langfuse**, **Arize Phoenix**) or managed (e.g., **LangSmith**, **Helicone**) tools to collect and store agent traces.
2. **Instrument your Agents** — Use **OpenLLMetry** or the framework's native SDK (like LangChain's LangSmith integration) to capture the "trace" of every LLM call, including the prompt, response, and tool usage.
3. **Capture "Tool Call" Spans** — Ensure that every action an agent takes (e.g., `git checkout`, `run test`, `write file`) is captured as a "span" in the trace, linked to the LLM call that triggered it.
4. **Monitor "Vitals"** — Track key metrics in real-time: token usage (cost), latency per step, error rates, and "loop detection" (identifying agents that are making the same call repeatedly).
5. **Enable Quality Feedback (Evals)** — Integrate **LLM-as-Judge Evaluation** scores directly into the observability platform to see which models or prompts are producing the highest quality outputs in production.

**Key observability metrics for agents:**

- **Latency** — Time per individual LLM call and time per overall task completion.
- **Cost** — Token usage and monetary cost per agent session.
- **Error Rates** — Refusals, timeouts, schema violations, and tool execution failures.
- **Agentic Loops** — Identifying agents that are stuck in an infinite "plan-act-fail" loop.
- **Output Quality** — Automated and human-provided scores for agentic outputs.

## Tradeoffs

**Pros:**

- Dramatically reduces the time and effort needed to debug complex, multi-step agentic failures.
- Provides a centralized "audit log" for compliance and security reviews of agent activity.
- Enables data-driven optimization of prompts and models to reduce cost and latency.

**Cons:**

- Traces can contain sensitive data (prompts, code, PII)—handle storage and access with extreme care.
- High-volume agentic systems can generate a massive amount of trace data, leading to high storage and processing costs.

**Difficulties:**

- Ensuring that all agents (including third-party tools like Claude Code or Devin) are correctly instrumented and sending data to the same platform.
- Managing the performance impact of instrumentation on latency-sensitive agent interactions.

## Rationale

Observability is the "black box recorder" of the agentic era. Without it, you are flying blind—you don't know why an agent failed, how much it cost, or whether its quality is improving or declining. Tracing turns "probabilistic" agentic behavior into a "deterministic" engineering artifact that can be analyzed, debugged, and optimized. For any team moving beyond simple experiments to real-world modernization, observability is not a "nice-to-have"; it is a foundational prerequisite for operational safety and reliability.

## Known Uses

- [Langfuse](https://langfuse.com/) — an open-source, self-hostable LLM observability platform that is popular for its strong tracing and evaluation capabilities.
- [LangSmith (LangChain)](https://www.langchain.com/langsmith) — a comprehensive platform for building, testing, and monitoring LangChain-based applications and agents.
- [Helicone](https://www.helicone.ai/) — a lightweight proxy-based observability tool that provides simple, effective tracing for any OpenAI-compatible API.

## References

- [OpenTelemetry — LLM Semantic Conventions](https://opentelemetry.io/docs/specs/otel/common/mapping-to-user-agents/llm/) — the industry-standard way to map LLM concepts to the OpenTelemetry model.
- [Arize Phoenix](https://phoenix.arize.com/) — an open-source observability tool that focus on the evaluation of RAG and agentic pipelines.

## Related Patterns

- [AI Gateway / Routing](ai-gateway-routing.md) — gateways are often the primary source of the data used for tracing and cost tracking.
- [LLM-as-judge Evaluation](llm-as-judge-evaluation.md) — the scores from the judge are a key metric to track in an observability platform.
- [Agentic Coding Workflows](agentic-coding-workflows.md) — observability is what makes these complex workflows debuggable and auditable.

## What Next

After instrumenting your first agent, implement [LLM-as-judge Evaluation](llm-as-judge-evaluation.md) to begin automatically scoring the quality of the outputs captured in your observability platform.

## Staging History

**Apply (Feb 2026):** LLM observability is a "day-one" requirement for any team using agentic tools on real codebases. The ability to audit, debug, and track the cost of agentic sessions is essential for moving from "vibes" to production-grade engineering.
