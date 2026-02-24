---
title: "Selective Modernization (Strategic Design)"
stage: apply
category: Legacy Modernization
description: "Categorizing subdomains into Core, Supporting, and Generic to focus agentic effort and high-quality design where it matters most for business value."
strategic_value: core
evolution: commodity
devops_phases: [plan, code]
---
## Problem

How do you prevent a modernization project from becoming a "death march" by trying to apply the same high level of quality, cost, and agentic reasoning to every part of a massive legacy system?

*This problem is difficult because:*

- Legacy systems are too large to modernize "perfectly" everywhere; trying to do so wastes limited budget, time, and human oversight.
- Without a strategic plan, teams (and AI agents) often spend excessive effort refactoring "low-value" supporting code while neglecting the "high-value" core logic.
- AI agents lack "common sense" regarding business priority—if tasked to "clean up the codebase," an agent will happily over-engineer a 20-year-old logging utility while ignoring a bug in the pricing engine.
- High-reasoning frontier models (like Claude 3.5 Sonnet) are expensive; using them for routine CRUD modernization is an inefficient use of the "Intelligence Budget."

*Yet, solving this problem is feasible because:*

- Eric Evans' **Strategic Domain-Driven Design** provides a framework for categorizing code into **Core**, **Supporting**, and **Generic** subdomains.
- AI agents can be "profiled" for specific subdomains: expensive, high-reasoning agents for the Core, and low-cost **Small Language Models (SLMs)** for Generic areas.
- **AI-assisted Codebase Analytics** can help human architects identify which modules have the highest "churn" and "complexity," signaling where the Core Domain actually lives.

## Solution

Utilize Strategic DDD to define the "Modernization Profile" for every module in your legacy system:

1. **Map the Subdomains** — Task a senior architect (human) to categorize the legacy codebase into three buckets:
    - **Core Domain** — The unique, high-value logic that gives the company a competitive advantage.
    - **Supporting Subdomain** — Necessary logic that is specific to the business but not a differentiator (e.g., custom report formats).
    - **Generic Subdomain** — Standard logic that could be handled by off-the-shelf software (e.g., auth, logging, standard CRUD).
2. **Assign the "Target Quality"** — Set different "Definition of Done" rules for each bucket:
    - **Core** — Hexagonal Architecture, 100% test coverage, meticulous **Context Engineering**, senior human review.
    - **Supporting/Generic** — Clean enough to maintain, standard MVC, basic test coverage, AI-driven review.
3. **Budget the Intelligence** — Assign your AI agents based on the subdomain:
    - **Core** — Frontier LLMs (Claude 3.5, GPT-4o) with complex **Agentic Orchestration Frameworks**.
    - **Generic** — **Small Language Models (SLMs)** or simple completion-based assistants.
4. **Enforce "Agent Guardrails"** — Use the subdomain map to set permissions: "Agents are only allowed to perform 'Extract Service' on Core modules; for Generic modules, only 'Rename' and 'Lint' are allowed."
5. **Protect the Core** — Use an **Anti-Corruption Layer (ACL)** to ensure that the Core Domain never depends on Supporting or Generic legacy mess.

## Tradeoffs

**Pros:**

- Ensures that the modernization budget is spent where it will have the greatest impact on business agility.
- Prevents "Architectural Paralysis" by accepting that some parts of the system will remain "good enough" rather than perfect.
- Optimizes token costs and human review time.

**Cons:**

- Requires deep business knowledge to correctly identify what is truly "Core."
- Mis-categorizing a module can lead to critical technical debt being ignored in what turns out to be a high-stakes area.

**Difficulties:**

- Resisting the urge to "fix everything"—developers often struggle with the discipline of leaving "messy but working" supporting code alone.
- Communicating these strategic boundaries to autonomous agents effectively.

## Rationale

Modernization is about the **Selective Allocation of Excellence**. As Eric Evans noted, "Not all of a large system will be well designed." By deliberately deciding where to invest in quality, you ensure that your "Target State" architecture remains lean and powerful. In the agentic era, this is even more critical: you must be the "Director" who tells the "Agent Army" which targets deserve surgical precision and which only need a routine patrol.

## Known Uses

- [Eric Evans — Strategic DDD](https://www.domainlanguage.com/ddd/strategic-design/) — the original formalization of subdomain types.
- [Wardley Mapping](https://learn.wardleymapping.com/) — a complementary strategic tool often used to identify which technical components are "Commodity" (Generic) vs "Genesis" (Core).

## References

- [Eric Evans — "Not all of a large system will be well designed" (QCon London 2008)](https://www.infoq.com/presentations/strategic-design-evans/) — the foundational talk for this practice.
- [Nick Tune — Strategic Domain-Driven Design](https://www.infoq.com/articles/ddd-strategic-design/) — a practical guide to mapping subdomains.

## Related Patterns

- [Domain-Driven Refactoring](../domain-driven-refactoring/) — the tactical counterpart; DDD refactoring is what you do *after* you've selected the target.
- [Small Language Models (SLMs)](../small-language-models/) — the primary tool for "low-value" subdomain modernization.
- [Anti-Corruption Layer](../anti-corruption-layer/) — used to isolate the Core Domain from the rest of the system.

## What Next

After mapping your subdomains, apply [Domain-Driven Refactoring](../domain-driven-refactoring/) specifically to your **Core Domain** to begin its deep modernization.

## Staging History

**Apply (Feb 2026):** Strategic Design is a foundational principle for any large-scale modernization. It is the only proven way to manage the "Intelligence Budget" of an agentic workforce and ensure modernization results in business value rather than just "cleaner" low-value code.
