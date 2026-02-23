---
title: "OpenTelemetry"
stage: apply
category: Architecture & Delivery
description: "Vendor-neutral distributed tracing, metrics, and logs. Necessary for understanding where AI-assisted systems are slow or failing."
strategic_value: generic
devops_phases: [operate, monitor]
---

## Overview

OpenTelemetry (OTel) is the CNCF standard for instrumentation: traces, metrics, and logs with a single, vendor-neutral API. Instrument once, export to any backend (Jaeger, Grafana Tempo, Datadog, Honeycomb, etc.).

## Why It Matters for AI-assisted Systems

AI agents introduce new failure modes — slow LLM calls, unexpected tool invocations, retries, context overflows. OTel gives you visibility into:
- Which LLM call in a multi-step agent is slow?
- Which tool is failing and with what error?
- How does end-to-end latency break down across services?

**OpenLLMetry** extends OTel with LLM-specific spans (token counts, model names, prompt/response).

## Getting Started

1. Add OTel SDK to each service
2. Auto-instrument frameworks (FastAPI, Spring, Django, etc.)
3. Deploy OTel Collector as a sidecar/daemon
4. Ship to a backend (start with Jaeger locally)

## Risks & Considerations

- Instrumentation adds a small performance overhead — negligible for most services
- Trace data volume can be high in production — sample appropriately
- OTel SDK APIs are stable but collector/exporter ecosystem still evolves

## Resources

- [OpenTelemetry documentation](https://opentelemetry.io/docs/) — official getting started guides per language
- [OpenLLMetry — LLM-specific OTel spans](https://github.com/traceloop/openllmetry) — extends OTel for AI observability
- [Grafana + Tempo — open-source tracing stack](https://grafana.com/oss/tempo/) — popular self-hosted OTel backend
