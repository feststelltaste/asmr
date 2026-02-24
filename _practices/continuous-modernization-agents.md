---
title: "Continuous Modernization Agents"
stage: trial
category: Agentic AI Tools
description: "Background 'Janitor' agents that incrementally pay down technical debt by updating dependencies, fixing linting errors, and improving tests on a schedule."
strategic_value: core
devops_phases: [code, build, operate]
---

# Continuous Modernization Agents

## Problem

How do you move from "modernization as a project" to "modernization as a process" that prevents technical debt from accumulating faster than you can pay it down?

*This problem is difficult because:*

- Modernization is traditionally treated as a one-time "big bang" project, which leads to a cycle of decay: the new system starts clean, but immediately begins accumulating debt.
- Developers are focused on "delivering features," leaving little time for the "janitorial" work of updating dependencies, fixing linting errors, and improving tests.
- Small, incremental improvements are often too tedious or "low value" for a senior developer to prioritize, so they are deferred until they become major architectural problems.
- Keeping a large, complex codebase "up-to-date" with the latest libraries, security patches, and coding standards is a full-time job that most teams cannot afford.

*Yet, solving this problem is feasible because:*

- AI "Janitor Agents" can run on a schedule (e.g., nightly) to identify and fix small, well-scoped modernization tasks autonomously.
- Agents are perfect for repetitive, mechanical "debt reduction" tasks that would bore a human developer but are critical for long-term system health.
- Modernization can be broken down into hundreds of small, automated PRs that humans can review and approve in seconds, rather than weeks.
- The cost of running an agent for a few hours each night is significantly lower than the cost of a developer performing the same work.

## Solution

Deploy background "Janitor Agents" that operate on a schedule to incrementally pay down technical debt:

1. **Identify "low-stakes" modernization tasks** — Focus on tasks that are well-scoped and easy to verify (e.g., "Update all `lodash` calls to use the native ES6 equivalents").
2. **Schedule the "Janitor Run"** — Set the agent to run during off-peak hours (e.g., every night or every weekend) to scan the repository for modernization opportunities.
3. **Execute via "Plan-Act-Verify"** — The agent identifies a task, creates a plan, makes the code changes, and runs the full test suite to ensure no regressions.
4. **Generate small, atomic Pull Requests** — The agent creates a PR for each individual improvement, including a clear description of the "why" and "how" of the change.
5. **Human-in-the-loop review** — Human developers treat the agent as a "junior developer," quickly reviewing and merging the PRs as part of their daily routine.

**Common "Janitor Agent" tasks:**

- **Dependency updates** — Moving beyond simple version bumps to refactoring code for breaking API changes.
- **Test gap filling** — Identifying untested functions in new PRs and automatically generating unit tests.
- **Pattern alignment** — If the team has adopted a new standard (e.g., `fetch` instead of `axios`), the agent incrementally refactors old files to match.
- **Linting and style fixes** — Systematically cleaning up formatting and "code smells" that the team has agreed to fix.
- **Dead code removal** — Incrementally deleting the "technically dead" code identified by static analysis.

## Tradeoffs

**Pros:**

- Prevents the "big bang" modernization trap by making improvement a continuous, low-cost activity.
- Ensures the codebase stays "evergreen" with the latest libraries and security patches.
- Reduces the cognitive load on human developers by handling the most boring parts of the job.

**Cons:**

- Can create "PR fatigue" if the agent produces too many noisy or low-value pull requests.
- Requires a high-quality CI/CD pipeline and comprehensive test suite to be safe.
- Token costs can add up if the agent is run too frequently on a very large codebase.

**Difficulties:**

- Ensuring the agent doesn't get stuck in a "refactoring loop" where it undoes its own changes or moves in circles.
- Balancing the agent's work with the human team's priorities: the agent shouldn't refactor code that a human is currently working on.

## Rationale

Continuous modernization is the only way to avoid the "legacy trap" where a system becomes too expensive to maintain after just a few years. AI agents change the economics of maintenance: by making the "janitorial" work nearly free, they allow teams to keep their codebase clean, modern, and secure indefinitely. This is the foundation of "sustainable software engineering" in the agentic era.

## Known Uses

- [Moderne / OpenRewrite](https://www.moderne.ai/) — a platform for large-scale, automated refactoring and modernization recipes that can be run on a schedule.
- [Dependabot / Renovate](https://github.com/dependabot) — the precursor to agentic janitors; they automate simple dependency bumps, but agentic versions can handle the actual code migration.
- [GitHub Copilot Extensions](https://github.com/features/copilot/extensions) — can be used to build custom, background agents for repo-specific modernization tasks.

## References

- [Adam Tornhill — Your Code as a Crime Scene](https://pragprog.com/titles/atcrime2/your-code-as-a-crime-scene-second-edition/) — the conceptual foundation for identifying where the "janitor" should focus its effort.
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg) — discusses the move toward persistent, autonomous agents in development.

## Related Patterns

- **Automated Dead Code Removal** — one of the primary tasks for a continuous modernization agent.
- **AI-powered Code Review** — the "first responder" that checks the agent's PRs before a human looks at them.
- **Agentic Coding Workflows** — the underlying technique used by the janitor agent to plan and execute its tasks.

## What Next

After establishing a "Janitor Agent," apply **AI-powered Code Review** to ensure its PRs are always high quality before they reach the human team.

## Staging History

**Trial (Feb 2026):** Continuous modernization agents are a powerful way to maintain long-term system health. However, they require a high-quality CI pipeline and careful tuning to avoid noisy PRs. Teams should start with very simple tasks (like dependency updates) before moving to complex pattern refactorings.
