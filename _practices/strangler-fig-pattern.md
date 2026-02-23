---
title: "Strangler Fig Pattern"
stage: apply
category: Legacy Modernization
description: "Incrementally replace a legacy system by routing traffic to new services while keeping the old system alive. The safest path for big-bang-free migration."
strategic_value: supporting
devops_phases: [plan, code, deploy, operate]
---

## Overview

Named after the strangler fig tree that grows around a host tree and eventually replaces it, this pattern wraps the legacy system with a routing layer, then incrementally redirects individual features to new implementations. The old system continues to run until it is fully replaced.

## How It Works

1. **Facade** — Place a proxy/router in front of the legacy system
2. **Intercept** — Route specific paths or features to new implementations
3. **Migrate** — Move functionality piece by piece, testing each
4. **Retire** — Once all traffic is routed, decommission the legacy system

## AI Acceleration

LLMs are now useful at every step:
- Analyzing legacy code to identify bounded contexts and seams
- Generating equivalent implementations in modern languages
- Writing integration tests to verify parity before switching traffic

## Risks & Considerations

- The facade layer adds latency and complexity
- Defining clean seams in a deeply coupled monolith is hard
- Requires discipline to not expand legacy dependencies during migration

## Resources

- [Martin Fowler — StranglerFigApplication](https://martinfowler.com/bliki/StranglerFigApplication.html) — the original pattern description
- [Sam Newman — Monolith to Microservices](https://www.oreilly.com/library/view/monolith-to-microservices/9781492047834/) — book covering strangler fig and related decomposition patterns
- [YouTube — Strangler Fig Pattern with AI assistance](https://www.youtube.com/results?search_query=strangler+fig+pattern+legacy+modernization+2025)
