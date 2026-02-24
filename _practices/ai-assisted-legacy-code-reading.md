---
title: "AI-assisted Legacy Code Reading"
stage: apply
category: Legacy Modernization
description: "Using LLMs to explain, document, and map unknown legacy code — COBOL, old Java, undocumented PHP. Dramatically reduces the 'understanding' phase."
strategic_value: core
devops_phases: [plan, code]
---

# AI-assisted Legacy Code Reading

## Problem

How do you accelerate the comprehension of unknown legacy code—COBOL, old Java, or undocumented PHP—when the original authors are gone and the documentation is non-existent?

*This problem is difficult because:*

- Legacy codebases often contain decades of "archeological layers" where different styles, frameworks, and implicit assumptions coexist.
- Reading and understanding complex code is significantly slower than writing it; a 500-line function with dense branching can take a developer hours to fully trace.
- Documentation for these systems is often outdated, misleading, or entirely missing, leaving the source code as the only reliable "source of truth."
- Subject matter experts (SMEs) are often a bottleneck—they spend more time answering "how does this work?" than performing the modernization work itself.

*Yet, solving this problem is feasible because:*

- Frontier LLMs (especially those with massive context windows like Gemini 1.5 Pro or Claude 3.5 Sonnet) can read and summarize thousands of lines of code in seconds, identifying patterns and business rules that would take a human developer days to map.
- LLMs can explain unfamiliar or archaic syntax (e.g., COBOL, PL/I, old Perl) in plain language, bridging the technical gap for modern developers.

## Solution

Utilize large context window LLMs to perform "software archaeology" on unknown legacy modules:

1. **Provide the full context** — Feed the LLM the entire module, including its configuration and call sites, rather than just isolated functions. Large context windows are essential for capturing cross-file dependencies.
2. **Ask for structured summaries** — Prompt the LLM to explain the code's intent (e.g., "What is the business logic inside this validation loop?") rather than just its mechanics.
3. **Map data flows and dependencies** — Use the AI to identify where data enters the system, how it is transformed, and which external tables or APIs it touches.
4. **Generate a domain glossary** — Ask the LLM to extract and define domain-specific terms it finds in variable names and comments.
5. **Identify entry points** — Use the AI to find the "main" entry points or the public API surface area of a large, undocumented monolith.

**Effective prompts for code reading:**

- "Explain this code to a senior developer who is new to the project."
- "What are the three most complex parts of this module, and why?"
- "Draw a Mermaid.js sequence diagram showing how a user request is processed by this module."
- "What are the implicit assumptions about the data format that this code makes?"

## Tradeoffs

**Pros:**

- Compresses weeks of manual "code archaeology" into hours.
- Enables modern developers to work effectively on archaic codebases without needing months of specialized training.
- Frees up subject matter experts (SMEs) from answering repetitive questions about how the code works.

**Cons:**

- LLMs can misread subtle, ambiguous logic—especially in languages with complex pointer arithmetic or global state.
- Summaries can be overly optimistic or miss "silent" error handling that is critical for production stability.

**Difficulties:**

- Ensuring the LLM has enough context to see the "big picture" without reaching the context limit or losing focus ("lost in the middle").
- Verifying the LLM's explanation against the actual behavior of the code, particularly for edge cases.

## Rationale

In any legacy modernization project, the "understanding" phase is the largest single cost and the greatest source of delay. Developers cannot safely refactor or replace what they do not understand. AI-assisted code reading changes the economics of modernization: by making the "archaeology" step nearly free, it allows teams to start making safe, informed changes much earlier in the project lifecycle. It is the essential "first step" that makes all subsequent modernization tasks possible.

## Known Uses

- [Sourcegraph](https://sourcegraph.com/) — provides code intelligence and search that helps developers navigate and understand large, complex codebases using AI.
- [GitHub Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — a standard tool for inline "explain this code" functionality that developers use daily.

## References

- [Michael Feathers — Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — the classic text on understanding legacy code; AI reading is a powerful modern implementation of these principles.
- [Approval Tests](https://approvaltests.com/) — a complementary technique; use AI to explain what the code *appears* to do, then use approval tests to verify what it *actually* does.

## Related Patterns

- [AI-generated Characterization Tests](ai-generated-characterization-tests.md) — the logical follow-up; once you understand the code with AI, use AI to generate the tests that prove it.
- [Knowledge Graph-Augmented Generation (GraphRAG)](knowledge-graph-augmented-generation.md) — for very large systems, a knowledge graph can help provide the "global" context that an LLM needs for accurate code reading.
- [AI Documentation Generation](ai-documentation-generation.md) — once the AI has explained the code, use it to generate the permanent documentation that was missing.

## What Next

After understanding the legacy module with AI assistance, apply [AI-generated Characterization Tests](ai-generated-characterization-tests.md) to create a safety net before attempting any changes.

## Staging History

**Apply (Feb 2026):** AI-assisted code reading is one of the most immediate and high-value applications of LLMs in software engineering today. It is a "low-risk, high-reward" practice that can be adopted by any team working on a legacy system with no specialized setup required.
