---
title: "Autonomous Pattern Enforcement"
stage: trial
category: Agentic AI Tools
description: "A multi-agent self-correction loop where a 'Guardian' agent monitors an 'Executor' agent, providing real-time feedback on convention violations to force autonomous improvement."
strategic_value: core
devops_phases: [code, test]
---

# Autonomous Pattern Enforcement

## Problem

How do you ensure that autonomously generated code follows project-specific conventions and architectural patterns without a human developer having to manually review and correct repetitive "stylistic" or "pattern" drift?

*This problem is difficult because:*

- AI agents naturally "drift" toward generic patterns found in their massive training data rather than the specific, idiosyncratic conventions of a particular legacy project (e.g., using a standard `fetch` call when the project requires a custom `LegacyAuthClient` wrapper).
- Project conventions are often "soft rules" that are hard to capture in traditional static analysis tools but are immediately obvious to a senior developer.
- If a human has to manually review every PR just to fix "style" or "convention" issues, the speed gains of using agents are lost to "review friction."
- Automated linters can flag errors, but they don't always provide the "architectural why" that an agent needs to correctly refactor its own approach.

*Yet, solving this problem is feasible because:*

- A multi-agent "Critic-Refiner" architecture allows one specialized agent (the **Guardian**) to monitor the work of another (the **Executor**).
- LLMs are excellent at "pattern matching" against a **Pattern Catalog** or a set of **Context Engineering** rules.
- The feedback loop can be integrated directly into the agent's "thinking" phase, forcing a self-correction cycle *before* the code is even saved to disk or submitted as a PR.

## Solution

Implement an automated "Self-Correction Loop" that pairs an Executor agent with a Guardian agent (or a specialized feedback engine):

1. **Define the Pattern Catalog** — Create a structured "Gold Standard" of your project's conventions (e.g., "Always use `Option` types for nullables," "All database queries must be wrapped in a `Repository`").
2. **Assign the Guardian Agent** — Deploy a second, independent agent whose only job is to compare the Executor's proposed changes against the Pattern Catalog and any executable **AI-driven Architectural Fitness Functions**.
3. **Execute the Feedback Loop** — When the Executor proposes a change, the Guardian intercepts it. If a violation is found, the Guardian sends a specific, instructional feedback message (e.g., "Violation: You used raw SQL. Correction: Refactor this to use the `OrderRepository` pattern as defined in our ADR").
4. **Autonomous Refinement** — The Executor receives the feedback, updates its plan, and re-implements the code. This cycle repeats until the Guardian provides a "Pass" verdict.
5. **PR Submission** — The code only reaches a human reviewer once it has been "certified" by the Guardian, ensuring the human only focuses on high-level business logic.

**Key components of the loop:**

- **The Pattern Catalog** — The "Rules of the Road" (see **Context Engineering**).
- **The Guardian** — The automated critic that enforces the rules.
- **The Feedback Prompt** — The structured instruction that tells the Executor *exactly* what to fix and why.

## Tradeoffs

**Pros:**

- Dramatically reduces "Reviewer Fatigue" by eliminating routine convention violations from the human review process.
- Ensures a much higher level of consistency across large-scale, multi-agent refactorings.
- Accelerates the agent's "learning" of a specific codebase's quirks through immediate, high-fidelity feedback.

**Cons:**

- Increases API token costs due to the iterative "Critic-Refiner" calls.
- Can lead to "Infinite Loops" if the Guardian and Executor disagree on a complex pattern or if the rule is ambiguous.

**Difficulties:**

- Writing "Guardian Prompts" that are firm enough to enforce patterns but flexible enough to allow for valid architectural edge cases.
- Balancing the latency of the self-correction loop with the developer's need for speed.

## Rationale

In the agentic era, "Linting" is no longer just about semicolons and indentation; it is about **Pattern Compliance**. Autonomous Pattern Enforcement shifts the "correction" step from the human review phase to the agentic execution phase. By making the agent responsible for its own quality control, teams can scale their modernization efforts to thousands of files while maintaining the same architectural rigor as a small, tightly-knit team of experts.

## Known Uses

- [RefAgent](https://arxiv.org/abs/2403.17134) — a research framework that uses specialized agents for planning, executing, and iteratively refining refactorings through self-reflection.
- [Devin / Claude Code](https://docs.anthropic.com/en/docs/claude-code) — these tools often include internal "verification steps" where the agent runs its own tests and linters to self-correct before presenting a result.

## References

- [Critic-Refiner Pattern](https://machinelearningmastery.com/multi-agent-collaboration-patterns/) — a foundational multi-agent collaboration pattern for iterative improvement.
- [Object-Oriented Reengineering Patterns](https://oorp.github.io/) — discusses the importance of consistent pattern adoption during reengineering.

## Related Patterns

- [Context Engineering](../context-engineering/) — the Pattern Catalog used by the Guardian is a primary output of context engineering.
- [AI-driven Architectural Fitness Functions](../ai-driven-architectural-fitness-functions/) — these functions provide the "executable" part of the Guardian's verification logic.
- [Agentic Coding Workflows](../agentic-coding-workflows/) — pattern enforcement is the "quality control" layer within a larger agentic workflow.

## What Next

After implementing basic pattern enforcement, apply [AI-driven Architectural Fitness Functions](../ai-driven-architectural-fitness-functions/) to add "hard" executable assertions to your Guardian agent's toolkit.

## Staging History

**Trial (Feb 2026):** Autonomous pattern enforcement is being trialed to reduce human review friction during large-scale agentic transformations. Using a 'Guardian' agent to provide real-time feedback has proven effective in keeping agents aligned with project-specific conventions.
