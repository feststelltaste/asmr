---
title: "AI Coding Assistants"
stage: stop
category: Agentic AI Tools
description: "GitHub Copilot, Cursor, Windsurf — using IDE-embedded AI tools to assist developers with localized code generation and explanation during modernization efforts."
strategic_value: supporting
devops_phases: [code]
---

## Problem

How do you accelerate the reading, comprehension, and modification of legacy codebases that are too large and underdocumented for any single developer to fully understand?

*This problem is difficult because:*

- Legacy codebases contain decades of implicit knowledge — naming is often inconsistent, logic is scattered, and the original developers are no longer available.
- Reading and understanding legacy code consumes the majority of a modernization engineer's time before any safe change can be made.
- Generating the necessary boilerplate for a modernization effort (adapters, mappers, test stubs, migration scripts) is unavoidable but tedious and error-prone.

*Yet, solving this problem is feasible because:*

- LLMs trained on vast code corpora can explain, summarize, and continue legacy code patterns without requiring full codebase comprehension.
- IDE-embedded assistants put this capability inline, providing immediate context-aware help during the development process.

## Solution

Inline AI coding assistants (e.g., GitHub Copilot, Cursor, Windsurf) integrate LLM capabilities directly into the development environment:

1. **Leverage code completion** to generate boilerplate (e.g., DTOs, getters, setters, or test stubs) that follows the established patterns in the current file.
2. **Utilize inline chat** to summarize unfamiliar functions or explain complex legacy logic during initial exploration.
3. **Apply localized refactoring tools** to rename variables or extract methods within a single file based on developer intent.
4. **Iterate on generated snippets** through a manual "prompt-review-accept" loop, where the developer drives every individual edit.

## Tradeoffs

**Pros:**

- Facilitates faster comprehension of unfamiliar legacy code and reduces friction for simple boilerplate generation.
- Lower barrier to entry for developers who are already familiar with the IDE.

**Cons:**

- Inline assistants treat legacy modernization as a series of disconnected, individual edits.
- They cannot reason across the full scope of a migration task, run tests to verify their own output, or coordinate changes across multiple files simultaneously.

**Difficulties:**

- Developers may build "prompt-then-accept" habits that lead to the uncritical acceptance of plausible-but-wrong suggestions for unfamiliar legacy APIs.
- These habits can also hinder the transition to more efficient agentic workflows.

## Rationale

Inline AI coding assistants were an important first step, demonstrating that LLMs could provide useful suggestions at the speed of editing. However, legacy modernization tasks are inherently multi-step and multi-file — such as extracting a service, updating all callers, and verifying with tests. Inline assistants require a human to manually drive every individual step in that sequence. 

In a legacy context, the bottleneck is rarely the individual keystroke; it is the coordination of correct changes across a complex system. Agentic tools (like Claude Code) address this by executing entire sequences from a single intent. Investing in inline assistant workflows for legacy modernization optimizes the wrong part of the process.

## Known Uses

- [GitHub — "Research: quantifying GitHub Copilot's impact on developer productivity and happiness" (2022)](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) — controlled study showing 55% faster task completion for routine coding tasks; notably limited to isolated, greenfield-style exercises rather than complex legacy modification.

## References

- [Simon Willison — AI-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/) — ongoing field notes from a prolific practitioner; documents the observed shift from inline completion toward agentic workflows as task complexity grows.
- [Kent Beck — "Exploring AI"](https://tidyfirst.substack.com/p/exploring-ai) — argues for maintaining test-first discipline when working with AI-generated code; the conceptual foundation for agentic TDD workflows.

## Related Patterns

- [Agentic Coding Workflows](agentic-coding-workflows.md) — the logical successor; agents that execute multi-step modernization tasks autonomously rather than requiring a human-driven loop for every change.
- [Human in the Loop](human-in-the-loop.md) — the review discipline established with inline assistants is foundational and should be maintained when transitioning to agentic workflows.
- [Agentic Orchestration Frameworks](agentic-orchestration-frameworks.md) — the infrastructure that enables more sophisticated autonomous agents to handle legacy codebase tasks.

## What Next

Transition to [Agentic Coding Workflows](agentic-coding-workflows.md) — utilizing tools that can autonomously plan and execute modernization goals across files, run tests, and manage version control directly.

## Staging History

**Stop (Feb 2026):** Agentic coding tools now handle multi-file edits, test runs, and PR creation autonomously, making the manual prompt-review-accept loop of inline assistants a significant bottleneck. Teams should move directly to agentic workflows rather than reinforcing habits centered on localized completions that will need to be unlearned.
