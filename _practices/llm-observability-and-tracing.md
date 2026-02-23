---
title: "LLM Observability & Tracing"
stage: trial
category: LLM Infrastructure
description: "Langfuse, LangSmith, Arize — tracking LLM calls, costs, latencies, and outputs in production. Necessary as soon as agents touch real workflows."
---

## Overview

LLM calls are opaque by default. Observability tooling captures traces of every prompt, response, tool call, and latency across an agentic workflow — enabling debugging, cost optimization, quality evaluation, and regression detection.

## Key Metrics to Track

- **Latency** per call and end-to-end
- **Token usage** and cost per workflow
- **Error rates** (refusals, timeouts, schema violations)
- **Output quality** (via LLM-as-judge or human review)
- **Cache hit rates** for prompt caching

## Tools

- **Langfuse** — Open-source, self-hostable LLM tracing
- **LangSmith** — LangChain ecosystem observability
- **Arize Phoenix** — Open-source, good for evaluation
- **Helicone** — Lightweight proxy-based tracing
- **OpenTelemetry** — Standard spans + [OpenLLMetry](https://github.com/traceloop/openllmetry) for LLM-specific traces

## Risks & Considerations

- Traces contain prompt data — handle PII carefully
- High-volume agentic systems generate a lot of trace data; control storage costs
- Start simple: even basic logging of prompts/responses is far better than nothing
