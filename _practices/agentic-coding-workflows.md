---
title: "Agentic Coding Workflows"
stage: trial
category: Agentic AI Tools
description: "Multi-step autonomous agents (Claude Code, Devin, OpenHands) that plan, write, run, debug, and iterate on tasks with minimal human guidance."
strategic_value: core
evolution: product
devops_phases: [plan, code, test]
---

# Agentic Coding Workflows

## Problem

How do you move beyond simple code completion to handle complex, multi-file modernization tasks that require planning, execution, and verification?

*This problem is difficult because:*

- Legacy modernization tasks (e.g., migrating a service to a new framework or refactoring a shared library) are rarely self-contained in a single file; they involve coordinated changes across dozens of files and call sites.
- A human developer manually driving every individual edit with a basic AI assistant becomes the bottleneck, spending more time on coordination and boilerplate than on high-value architectural decisions.
- Verifying that a large-scale change hasn't introduced regressions requires a tight, repetitive loop of "edit-compile-test" that is slow and error-prone for humans to perform manually across a large system.

*Yet, solving this problem is feasible because:*

- Frontier LLMs have developed the reasoning capability to plan multi-step sequences and use tools (shell, file system, compilers) to execute them.
- Agentic loops can autonomously handle the repetitive "mechanical" work of modernization—renaming, moving, and updating—while reporting back for human guidance only when they encounter ambiguity or high-risk decisions.

## Solution

Deploy autonomous AI agents that operate directly on the codebase, using a "plan-act-verify" loop to complete modernization goals:

1. **Define a clear goal** — provide the agent with a high-level intent (e.g., "Migrate all JUnit 4 tests in the `payment` module to JUnit 5 and ensure they pass").
2. **Let the agent plan** — the agent explores the codebase, identifies the scope of change, and proposes a multi-step sequence of actions.
3. **Execute via tool use** — the agent uses shell and file system tools to make changes, compile code, and run tests.
4. **Autonomous debugging** — when a test fails or a build breaks, the agent reads the error output and iterates on its own solution without human intervention.
5. **Human-in-the-loop review** — the developer reviews the final PR or the session transcript, providing a final quality gate before the change is merged.

## Tradeoffs

**Pros:**

- Dramatically increases the speed of mechanical modernization tasks.
- Agents can work in parallel on different modules, accelerating the overall migration timeline.
- The "edit-compile-test" loop is executed with higher frequency and consistency than a human developer.

**Cons:**

- Vague goals or poorly specified constraints can lead to "agent drift," where the agent makes unnecessary or incorrect changes.
- Agents can consume significant API tokens if they get stuck in an infinite debugging loop.

**Difficulties:**

- Setting up the necessary environment (compilers, test runners, sandboxes) so the agent can actually run the code it is modifying.
- Monitoring agent progress without becoming the bottleneck yourself requires a shift in developer mindset from "coder" to "orchestrator."

## Rationale

In legacy modernization, the bottleneck is rarely the individual keystroke; it is the coordination of correct changes across a complex system. Agentic workflows shift the developer's role from manual executor to strategic reviewer. By allowing an agent to handle the high-volume, repetitive parts of a migration—while keeping a human in the loop for architectural decisions—teams can tackle modernization projects that were previously considered too expensive or time-consuming to attempt.

## Known Uses

- [SWE-bench](https://www.swebench.com/) — an industry-standard benchmark where agents like Devin and Claude Code are evaluated on their ability to solve real-world GitHub issues autonomously.
- [OpenHands (formerly OpenDevin)](https://github.com/All-Hands-AI/OpenHands) — a community-driven platform used by modernization teams to build custom agentic pipelines for large-scale refactoring.

## References

- [Anthropic — Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) — documentation for the terminal-based agent that demonstrates the power of direct shell and file system access.
- [Cognition — Devin](https://cognition.ai/) — the first widely publicized autonomous AI software engineer, establishing the category of agentic coding.

## Related Patterns

- [Agent Sandboxing](../agent-sandboxing/) — a prerequisite for safely running agentic workflows that have shell and file system access.
- [Human in the Loop](../human-in-the-loop/) — the critical quality gate that makes autonomous agent work trustworthy in a production codebase.
- [AI-generated Characterization Tests](../ai-generated-characterization-tests/) — provides the safety net that agents need to refactor legacy code without fear of regression.

## What Next

Once comfortable with basic agentic workflows, implement [Agent Sandboxing](../agent-sandboxing/) to ensure these agents can run and test code in a secure, isolated environment without risking the host system.

## Staging History

**Trial (Feb 2026):** Multi-step agentic workflows are showing high potential for automating repetitive modernization tasks. While the technology is maturing rapidly, teams should continue trialing these workflows on well-scoped modules to establish reliable human-in-the-loop patterns before broad application.
