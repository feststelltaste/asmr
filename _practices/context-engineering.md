---
title: "Context Engineering"
stage: apply
category: Agentic AI Tools
description: "Designing the information environment for AI agents — project rules files, architecture docs, and conventions that help AI understand your codebase and produce better output."
strategic_value: core
devops_phases: [plan, code]
---

# Context Engineering

## Problem

How do you design and maintain the "information environment" that an AI agent needs to understand your unique legacy codebase, follow your specific conventions, and produce high-quality modernization output?

*This problem is difficult because:*

- Legacy codebases are often inconsistent—different modules follow different styles, frameworks, and naming conventions from different eras of development.
- Standard LLMs only "see" the files they are given; without explicit context, they will "hallucinate" solutions based on their generic training data rather than your project's specific architectural rules.
- Providing "too much context" can confuse an agent (the "lost in the middle" problem), while "too little context" leads to plausible-but-wrong decisions that require human cleanup.
- Project conventions and architectural rules are often "tribal knowledge" that isn't documented in the code itself, making them invisible to an AI agent.

*Yet, solving this problem is feasible because:*

- Frontier LLMs can follow complex, high-level instructions provided in "system prompts" or "rules files" (like `CLAUDE.md`, `.cursorrules`, or `.github/copilot-instructions.md`) that define the project's unique constraints.
- Dedicated context engineering—the practice of crafting concise, high-signal instructions and examples—can dramatically improve an agent's accuracy on its first attempt.
- Context can be layered: global architectural rules for the entire repository can be combined with specific directory-level rules for individual modules or services.

## Solution

Deliberately engineer the "memory" and "instructions" for your AI agents to ensure they align with your modernization goals:

1. **Establish a project rules file** — Create a `CLAUDE.md`, `.cursorrules`, or similar file in the project root that defines the "ground rules" for all AI interactions (e.g., "Always use the `TaxService` for calculations, never call the database directly").
2. **Draft a concise architecture summary** — Provide a high-level overview of the system's bounded contexts, key data flows, and "target state" architecture so the agent understands where the project is heading.
3. **Curate a domain glossary** — Define domain-specific terms (e.g., "An 'Order' is always in state 'DRAFT' before 'CONFIRMED'") to ensure the AI uses the correct terminology in its generated code.
4. **Provide "Gold Standard" examples** — Include a few small, perfect examples of the modern code you want the agent to produce (e.g., "This is how a modern repository should look in our new system").
5. **Layer context for scale** — In a large monorepo, use directory-level rules files to provide module-specific context without overwhelming the agent with global rules.

**Key artefacts for Context Engineering:**

- **Project Rules File** (`CLAUDE.md`, `.cursorrules`) — the "brain" of the agent's interaction.
- **Architecture Overview** — the "map" for the modernization journey.
- **Domain Glossary** — the "dictionary" for ubiquitous language.
- **Example Snippets** — the "blueprints" for the target state.

## Tradeoffs

**Pros:**

- Dramatically improves the accuracy and "first-time quality" of AI-generated code.
- Reduces the manual effort of correcting common mistakes the agent makes due to lack of context.
- Provides a centralized, version-controlled source of truth for both human and AI developers.

**Cons:**

- Stale context is worse than no context—if the rules file is not updated as the architecture evolves, the AI will consistently produce "wrong" code.
- Over-engineering: extremely long or complex rules files can actually degrade the LLM's performance by diluting its focus.

**Difficulties:**

- Writing concise, high-signal rules that an LLM can reliably follow without ambiguity.
- Ensuring that all developers (human and AI) are aware of and following the engineered context.

## Rationale

The quality of AI-generated code is determined as much by the *environment* in which the AI operates as by the model itself. In a legacy context, where "the way we do things" is often undocumented and inconsistent, context engineering is the only way to give an agent a fighting chance at producing idiomatic, high-quality code. It is the "software architecture" of the agentic era—defining the constraints and patterns that allow autonomous agents to work safely and effectively at scale.

## Known Uses

- [Anthropic — CLAUDE.md memory](https://docs.anthropic.com/en/docs/claude-code/memory) — the official specification for the "memory" file that the Claude Code agent uses to maintain project-specific context.
- [Cursor Rules](https://docs.cursor.com/context/rules-for-ai) — a widely used system for providing custom instructions to an IDE-based AI assistant.
- [Copilot Instructions](https://docs.github.com/en/copilot/using-github-copilot/customizing-copilot-to-improve-suggestions) — a similar system for the GitHub Copilot ecosystem.

## References

- [Philipp Schmid — Context Engineering](https://www.philschmid.de/context-engineering) — a practical look at how to shape LLM behavior through dynamic context construction.
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg) — discusses the move from "prompting" to "engineering the environment" for agents.

## Related Patterns

- [Harness Engineering](harness-engineering.md) — context is what the agent *knows*; the harness is what the agent can *do* and how it *verifies* its work.
- [Agentic Coding Workflows](agentic-coding-workflows.md) — the workflow provides the "dynamic" context (current task, error logs), while context engineering provides the "static" context (architectural rules).
- [Human in the Loop](human-in-the-loop.md) — review is the primary feedback loop for updating the engineered context (e.g., "The AI keeps making this mistake, let's add a rule for it").

## What Next

After establishing your first project rules file, implement [Harness Engineering](harness-engineering.md) to build the execution environment where the agent can run and verify the code it writes based on those rules.

## Staging History

**Apply (Feb 2026):** Context engineering is a "must-have" for any team using agentic tools on a legacy codebase. It is the primary lever for improving agent quality and should be established as soon as an agentic tool is introduced into the project.
