---
title: "Sprout and Bubble"
stage: apply
category: Legacy Modernization
description: "Adding new functionality by creating fresh, clean code ('Sprouting') and containing it within a protected 'Bubble Context' to prevent legacy patterns from polluting modern logic."
strategic_value: core
devops_phases: [plan, code]
---
## Problem

How do you add new features or modern logic to a "big ball of mud" legacy system without making the technical debt worse or forcing the agent to navigate thousands of lines of existing spaghetti code?

*This problem is difficult because:*

- Editing complex legacy functions is high-risk: even a small change can trigger a cascade of "invisible" side effects.
- AI agents are significantly more accurate when writing fresh code than when trying to "merge" logic into existing, messy implementations.
- New code that is directly embedded in legacy classes often adopts the same "bad" naming, structures, and coupling as the surrounding code.
- Traditional "in-place" development leads to a slow degradation of the new system before it's even finished.

*Yet, solving this problem is feasible because:*

- **Sprouting** (Method or Class) allows you to implement new logic in a 100% clean, independent unit and simply call it from the legacy code.
- A **Bubble Context** (or "Clean Room") provides a strategic boundary where new agent-driven development can happen using modern standards, independent of legacy constraints.
- Agents are highly efficient at "scaffolding" these clean zones and generating the "wrapper" or "bridge" code needed to connect them to the old system.

## Solution

Utilize Sprout techniques to build a "Bubble Context" for all new agentic development:

1. **Sprout Method / Class** — When adding a feature, do not edit the legacy function. Instead, task an agent to "Sprout" a new, independent method or class that implements the new logic cleanly.
2. **Bridge the Gap** — Add a single, minimal call site in the legacy code that delegates to the new sprouted unit.
3. **Establish the Bubble** — Define a new package, module, or service (The Bubble) where all new code must reside. This bubble follows your modern **Context Engineering** rules.
4. **Protect with an ACL** — Place an **Anti-Corruption Layer** at the edge of the bubble to translate legacy data structures into clean domain objects for the new code.
5. **Grow the Bubble** — As more features are added, "sprout" them into the bubble. Over time, the bubble grows until it eventually replaces the legacy system (see **Strangler Fig Pattern**).

**Sprouting Patterns for Agents:**

- **Sprout Method** — Moving a new logic block into its own method to make it testable in isolation.
- **Sprout Class** — Creating a new class for a new responsibility, keeping the legacy class as a thin "proxy."
- **Wrap Method / Class** — Adding logic "around" a legacy call rather than inside it.

## Tradeoffs

**Pros:**

- Minimizes the risk of breaking existing logic by reducing the "touch points" in legacy code.
- Allows agents to work at 100% velocity in a clean, modern environment.
- Ensures that the "new" part of the system is maintainable and decoupled from the start.

**Cons:**

- Can lead to "fragmentation" where the system's logic is split between many small, sprouted units and the legacy core.
- Requires discipline to ensure the "bubble" doesn't get breached by legacy shortcuts.

**Difficulties:**

- Passing complex legacy state (e.g., a massive global object) into a clean sprouted method without polluting its interface.
- Handling cross-cutting concerns (logging, security) that are handled differently in the old vs. new code.

## Rationale

In legacy modernization, "Stop the Bleeding" is the first priority. **Sprouting** ensures that every new line of code added to the system is better than the last. For AI agents, this is the only reliable way to maintain high autonomy: by giving the agent a "clean room" (the Bubble) to work in, you remove the noise and risk of the legacy environment, allowing for deterministic, high-quality output.

## Known Uses

- [Michael Feathers — Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — introduced Sprout Method and Sprout Class as the safest ways to add features.
- [Domain-Driven Design (Blue Book)](https://www.domainlanguage.com/ddd/) — discusses the concept of a "Bubble" or "Bounded Context" as a strategic modeling tool.

## References

- [Michael Feathers — "Sprout Method"](https://workingeffectivelywithlegacycode.com/) — (Historical) the classic technique for safe incremental change.
- [Eric Evans — Strategic Design: Context Mapping](https://www.domainlanguage.com/ddd/context-mapping/) — the conceptual foundation for the Bubble Context.

## Related Patterns

- [Context Engineering](context-engineering.md) — defines the rules that apply inside the bubble.
- [Anti-Corruption Layer](anti-corruption-layer.md) — the "skin" of the bubble that protects it from legacy corruption.
- [Strangler Fig Pattern](strangler-fig-pattern.md) — the bubble is the starting point for a strangler fig migration.

## What Next

After sprouting your first modern capability, apply [Anti-Corruption Layer](anti-corruption-layer.md) to formalize the boundary of your new Bubble Context.

## Staging History

**Apply (Feb 2026):** Sprouting is the safest and most effective way for agents to add functionality to legacy systems. It has become a standard "agentic maneuver" for preventing technical debt from worsening during long-running modernization projects.
