---
title: "AI-driven Architectural Fitness Functions"
stage: assess
category: Legacy Modernization
description: "Using agents to automatically write and execute tests that enforce architectural boundaries and prevent newly refactored code from drifting back into legacy patterns."
strategic_value: core
devops_phases: [plan, test]
---

# AI-driven Architectural Fitness Functions

## Problem

How do you prevent a newly refactored system from "drifting" back into legacy patterns and ensure that strict architectural boundaries—like an Anti-Corruption Layer—are actually maintained over time?

*This problem is difficult because:*

- Architectural rules (e.g., "The Payment service must never call the User database directly") are often documented in wikis or ADRs but rarely enforced in code, leading to silent regressions.
- Manual code review is an imperfect gate for architectural compliance; reviewers often miss subtle coupling that violates the intended target state.
- In a large-scale modernization, dozens of agents and developers are making changes simultaneously; without automated governance, the system's "entropy" increases faster than it can be managed.
- Traditional "Fitness Function" tools (like ArchUnit or NetArchTest) require manual authoring of complex rules that many teams find too tedious to maintain as the architecture evolves.

*Yet, solving this problem is feasible because:*

- AI agents can read architectural intent from ADRs or natural language descriptions and automatically translate them into executable fitness functions.
- LLMs can analyze codebase-wide dependency graphs and identify violations of "layered" or "hexagonal" architectures that are invisible to simple linters.
- Agents can run as part of the CI/CD pipeline, acting as an "Architectural Janitor" that automatically flags (or fixes) code that bypasses the defined boundaries.

## Solution

Deploy AI agents to define, execute, and maintain automated architectural assertions across your codebase:

1. **Codify Architectural Intent** — Task an agent to read your Architecture Decision Records (ADRs) and extract core constraints (e.g., "No circular dependencies between Bounded Contexts").
2. **Generate Executable Tests** — Use an LLM to generate tests using tools like **ArchUnit** or **Semgrep** that programmatically assert these constraints.
3. **Analyze Multi-File Dependencies** — Use an agent to perform "Deep Dependency Analysis" that identifies non-obvious coupling, such as shared global state or implicit database-level dependencies.
4. **Enforce at the PR Gate** — Integrate the fitness functions into the CI/CD pipeline. Use an **AI-powered Code Review** bot to explain architectural violations to developers and suggest fixes.
5. **Evolve the Rules Autonomously** — As the modernization progresses and new bounded contexts are defined, task an agent to update the fitness functions to reflect the "new" target state.

**Common Fitness Function assertions:**

- **Layer Integrity** — "The Domain layer must not depend on the Infrastructure layer."
- **Bounded Context Isolation** — "Service A must only communicate with Service B via its public API/Events."
- **Pattern Compliance** — "All data access in the refactored module must use the Repository pattern."
- **Legacy Containment** — "No new code may call classes located in the `com.legacy.*` package."

## Tradeoffs

**Pros:**

- Provides continuous, automated governance that ensures the architecture actually improves over time.
- Reduces the "cognitive load" on human architects by automating the enforcement of routine patterns.
- Prevents "modernization decay" where refactored code slowly becomes as messy as the legacy code it replaced.

**Cons:**

- If the fitness functions are too rigid, they can slow down development and lead to "rule-bending" by developers.
- AI-generated rules can sometimes produce false positives if they misinterpret the architectural intent.

**Difficulties:**

- Translating "fuzzy" architectural concepts (like "high cohesion") into precise, executable code assertions.
- Keeping the fitness functions in sync with a rapidly changing "target state" during an active modernization.

## Rationale

Modernization is not a one-time event; it is an evolutionary process. Without automated "governance," even the most perfectly refactored system will eventually succumb to entropy and become the next generation's legacy debt. AI-driven fitness functions change the economics of governance: they make it nearly free to define and enforce the "rules of the game," allowing teams to scale their modernization efforts without sacrificing architectural integrity.

## Known Uses

- [ArchUnit](https://www.archunit.org/) — a Java library for asserting architectural rules; many teams now use AI to generate and maintain ArchUnit test suites.
- [Semgrep](https://semgrep.dev/) — used to write custom static analysis rules that enforce architectural patterns across multiple languages.

## References

- [Neal Ford, Rebecca Parsons, Patrick Kua — *Building Evolutionary Architectures*](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) — introduced the concept of architectural fitness functions as a primary tool for managing change.
- [Object-Oriented Reengineering Patterns](https://oorp.github.io/) — discusses the importance of architectural "checks" during the reengineering process.

## Related Patterns

- [Anti-Corruption Layer](anti-corruption-layer.md) — fitness functions are the primary tool for ensuring the ACL boundary is not breached.
- [AI-driven Technical Debt Detection](ai-technical-debt-detection.md) — debt detection finds the problems; fitness functions prevent them from coming back.
- [Continuous Modernization Agents](continuous-modernization-agents.md) — these agents use fitness functions as their "definition of done" for refactoring tasks.

## What Next

After establishing your first set of fitness functions, implement [Continuous Modernization Agents](continuous-modernization-agents.md) to automatically fix the violations the functions identify.

## Staging History

**Assess (Feb 2026):** AI-driven architectural governance is an emerging but critical practice for enterprise-scale modernization. While the underlying tools are mature, using LLMs to autonomously define and evolve the "rules" is a new capability that teams should assess for their most critical modernization targets.
