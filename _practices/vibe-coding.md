---
title: "Vibe Coding"
stage: trial
category: Agentic AI Tools
description: "AI-first development where you describe intent in natural language and let the AI implement, then iterate on the result rather than writing code line by line."
strategic_value: core
devops_phases: [code]
---

# Vibe Coding

## Problem

How do you accelerate the initial prototyping and exploration of a legacy modernization project without getting bogged down in the syntax, boilerplate, and "manual friction" of a new language or framework?

*This problem is difficult because:*

- Modernization often involves moving to a new, unfamiliar stack (e.g., COBOL to Java 21, or Java 8 to Go), which has a steep "learning curve" for the developer.
- Developers spend more time on "ceremony" (setting up build scripts, writing DTOs, configuring libraries, and managing imports) than on the actual business logic of the new system.
- The "fear of making a mistake" in an unfamiliar language can lead to slow, overly cautious development that delays the project.
- Traditional "line-by-line" coding is an expensive and time-consuming way to explore multiple architectural options or "proof-of-concepts" for a new system.
- Modernization teams are often "pushed" to deliver results quickly, but the manual effort of writing everything from scratch is the primary bottleneck.

*Yet, solving this problem is feasible because:*

- **Vibe Coding** (a term coined by Andrej Karpathy) is an AI-first programming style where you express *what* you want in natural language and let the AI generate the implementation.
- Frontier LLMs are highly proficient in all major modern languages and frameworks, allowing them to "scaffold" a new project or service in seconds.
- You can iterate at a higher level of abstraction by describing changes ("Now add an error handler for the API call," "Refactor this to use the repository pattern") rather than writing each individual line manually.
- You are the "Director"; the AI is the "Implementer." You provide the "vibe" (the intent), and the AI handles the mechanical details.

## Solution

Adopt a "Vibe Coding" approach for the initial exploration and prototyping of your modernization project:

1. **Describe the "Vibe"** — Use natural language to describe the goal of the new service or module (e.g., "Build a new Go service that reads from this legacy DB table and exposes a REST API for the 'billing' context").
2. **Scaffold with AI** — Let the AI generate the initial boilerplate, directory structure, and basic business logic in your target stack.
3. **Iterate via "Conversation"** — Instead of editing the code manually, provide the AI with feedback and refinement requests (e.g., "Now add a JSON-RPC interface for internal calls," "Ensure all errors are logged to our central system").
4. **Focus on Architectural Judgment** — Spend your cognitive energy on judging whether the AI's implementation is correct, idiomatic, and follows your **Context Engineering** rules.
5. **Feed Failures Back** — If the AI-generated code fails to compile or run, paste the error output directly into the chat and let the AI "self-correct" (autonomous debugging).

**When "Vibe Coding" is most effective:**

- **Prototyping and exploration** — Trying an idea quickly without the overhead of manual scaffolding.
- **Unfamiliar technology** — Letting the AI handle the "syntax" while you focus on the "logic."
- **High-volume transformations** — "Apply this specific pattern to all 40 of these files at once."
- **Well-scoped tasks** — When the goal is clear and the AI can be constrained with high-quality prompts.

## Tradeoffs

**Pros:**

- Dramatically increases the speed of initial development and prototyping for a new system.
- Reduces the "cognitive load" of switching to an unfamiliar language or framework.
- Allows developers to focus on high-level architecture and domain correctness rather than syntax.

**Cons:**

- High risk of "hallucinations" and "technically correct but architecturally wrong" solutions if the agent is not perfectly constrained.
- Can lead to a "blindly accept" habit where developers stop reading the code carefully (the "rubber stamping" problem).

**Difficulties:**

- Developing the "prompting skill" needed to provide the AI with a clear, unambiguous "vibe" that it can follow.
- Ensuring the AI-generated "vibe" code is actually testable and maintainable for the long term.

## Rationale

Vibe Coding is the "high-velocity" layer of the agentic stack. For legacy modernization, it is the tool that breaks the "architectural paralysis"—it allows teams to quickly "try out" different designs and technologies before committing to a final path. It is not about "not coding"; it is about coding at a higher level of abstraction, using AI as the "junior engineer" that handles the tedious parts while you provide the strategic direction.

## Known Uses

- [Andrej Karpathy — "Vibe Coding"](https://x.com/karpathy/status/1886192184808149176) — the original post that named this AI-first programming style.
- [Cursor IDE](https://cursor.com/) — a popular AI-native IDE that is specifically designed for "vibe-style" iteration on code.
- [Replit Agent](https://replit.com/ai) — an autonomous agent that can build entire applications from a natural language prompt.

## References

- [Ethan Mollick — Co-Intelligence](https://www.oneusefulthing.org/) — practical guidance on working with AI as a partner in complex tasks.
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg) — a critical look at the limitations of "vibes" in large-scale legacy environments.

## Related Patterns

- [Agentic Coding Workflows](agentic-coding-workflows.md) — vibe coding is the "interactive" version of an agentic workflow.
- [Context Engineering](context-engineering.md) — the "vibe" is only as good as the context (rules, architecture docs) you provide the AI.
- [Harness Engineering](harness-engineering.md) — for high-stakes projects, "vibe coding" must be paired with a "harness" to ensure correctness.

## What Next

After prototyping your first service with [Vibe Coding](vibe-coding.md), implement [Harness Engineering](harness-engineering.md) to build the structured environment where the "vibe" code can be properly tested and verified.

## Staging History

**Trial (Feb 2026):** Vibe coding is a powerful technique for exploration and prototyping. However, it should be used with caution for "production-critical" legacy code. Teams should trial it on low-stakes projects or for initial scaffolding before moving to more structured **Agentic Coding Workflows** for the core modernization work.
