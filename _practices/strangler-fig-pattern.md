---
title: "Strangler Fig Pattern"
stage: apply
category: Legacy Modernization
description: "Incrementally replace a legacy system by routing traffic to new services while keeping the old system alive. The safest path for big-bang-free migration."
strategic_value: supporting
evolution: commodity
devops_phases: [plan, code, deploy, operate]
---

# Strangler Fig Pattern

## Problem

How do you replace a massive, mission-critical legacy monolith without a high-risk "big bang" rewrite that would take years to complete and could cause catastrophic production failures?

*This problem is difficult because:*

- Legacy monoliths are "too big to fail"—they are deeply coupled, poorly understood, and have thousands of "undocumented" business rules that are hard to replicate from scratch.
- A "big bang" rewrite (starting from scratch) is the most common cause of modernization failure: the business loses patience before the new system is ready to go live.
- "Feature parity" is a moving target: as you rewrite the old system, new requirements are added to it, making the "finish line" constantly recede as you build.
- Direct database sharing between the legacy and modern systems is a high-risk "anti-pattern" that leads to data corruption and tight coupling, preventing true independence.
- The "fear of the unknown" keeps teams from touching critical modules, leading to a state of "architectural paralysis."

*Yet, solving this problem is feasible because:*

- The **Strangler Fig Pattern** allows for an "incremental" migration where individual features or modules are "strangled" from the monolith and moved to new services one by one.
- AI agents can accelerate every step of the strangler fig: identifying the logical "seams" in the code, generating equivalent implementations in modern languages, and writing the integration tests to prove functional parity.
- Routing layers and API gateways (like NGINX, Kong, or custom proxies) allow for the transparent, side-by-side execution of old and new code during the transition.
- Modernization can be prioritized by "business value," delivering new features in the modern system while the legacy monolith is still running.

## Solution

Implement an incremental migration using a routing layer to "strangle" the legacy monolith slice by slice:

1. **Establish a Facade** — Place a proxy/router in front of the legacy monolith to intercept all incoming requests (API, web, or message).
2. **Identify the first "Seam"** — Use **Domain-Driven Refactoring** and **AI-assisted Codebase Analytics** to find a well-scoped, high-value feature that can be extracted with minimal dependencies.
3. **Build the New Service** — Implement the extracted feature in your modern target stack. Protect it with an **Anti-Corruption Layer (ACL)** to prevent legacy concepts from bleeding in.
4. **Synchronize the Data** — Use "Event Interception" or "Change Data Capture (CDC)" to keep the data in sync between the old and new systems during the transition.
5. **Redirect the Traffic** — Configure the facade to route requests for the extracted feature to the new service. Use **AI-powered Code Review** and **Canary Deployments** to ensure a safe rollout.
6. **Retire and Repeat** — Once the new service is stable, decommission the corresponding logic in the legacy monolith. Repeat the process for the next feature until the monolith is gone.

**Key Strangler Fig stages:**

- **Transform** — Building the new feature in the modern stack.
- **Coexist** — Running both old and new implementations side-by-side.
- **Eliminate** — Removing the legacy implementation once the new one is proven.

## Tradeoffs

**Pros:**

- Dramatically reduces the risk of failure compared to a "big bang" rewrite.
- Delivers business value early and often by modernizing the most important features first.
- Provides a continuous feedback loop that allows the team to learn and adjust their modernization strategy as they go.

**Cons:**

- Increases the complexity of the architecture during the migration (due to the facade and data sync).
- The "strangling" process can take a long time, leading to a state of "two systems" that must be maintained simultaneously.

**Difficulties:**

- Untangling the "shared database" that often binds different parts of a monolith together.
- Ensuring functional parity between the old and new systems for complex, undocumented edge cases.

## Rationale

The Strangler Fig is the "industry standard" for safe legacy modernization. It is named after the strangler fig tree that grows around a host tree and eventually replaces it, leaving only a hollow trunk. In a software context, it allows for a "risk-managed" transition where the old system provides the safety net for the new. AI agents turn this from a "years-long" manual effort into a "months-long" automated process, making it the primary pattern for any large-scale modernization program.

## Known Uses

- [Martin Fowler — StranglerFigApplication](https://martinfowler.com/bliki/StranglerFigApplication.html) — the original pattern description that has become the foundational text for legacy migration.
- [Sam Newman — Monolith to Microservices](https://www.oreilly.com/library/view/monolith-to-microservices/9781492047834/) — a comprehensive book covering the strangler fig and related patterns for system decomposition.

## References

- [Microsoft Azure — Strangler Fig Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — architectural guidance on implementing the pattern in a cloud environment.
- [Google Cloud — Modernizing Monolithic Applications](https://cloud.google.com/architecture/modernizing-monolithic-applications-to-microservices) — a guide to using strangler fig for cloud-native migrations.

## Related Patterns

- [Anti-Corruption Layer](../anti-corruption-layer/) — the primary technical pattern for protecting the new "strangler" service from legacy data corruption.
- [Domain-Driven Refactoring](../domain-driven-refactoring/) — provides the "cuts" for the slices that are strangled from the monolith.
- [AI-generated Characterization Tests](../ai-generated-characterization-tests/) — provides the safety net needed to prove functional parity before switching traffic to the new service.

## What Next

After identifying your first "seam," apply [Anti-Corruption Layer](../anti-corruption-layer/) to protect your new service as you begin to migrate the logic from the monolith using the [Strangler Fig Pattern](../strangler-fig-pattern/).

## Staging History

**Apply (Feb 2026):** The Strangler Fig Pattern is the industry-standard, well-proven choice for safe monolith decomposition. Its incremental nature is a perfect match for agentic workflows, which can autonomously modernize and verify individual 'slices' of the legacy system.
