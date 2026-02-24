---
title: "Structured LLM Output (JSON mode)"
stage: trial
category: AI Tooling Setup
description: "Enforcing typed JSON schemas on LLM output (tool use, JSON mode). Makes LLMs reliable participants in typed software pipelines."
strategic_value: generic
evolution: product
devops_phases: [code, build]
---

# Structured LLM Output

## Problem

How do you reliably and consistently integrate LLM outputs—like refactoring plans, data extracts, or migration scripts—into automated software pipelines that require strictly typed data formats?

*This problem is difficult because:*

- LLMs are inherently "probabilistic" and "conversational"—they often produce free-form text, explanations, and "chatter" that are difficult for downstream software to parse.
- "Plausible but malformed" JSON is a common failure mode: an LLM might miss a comma, misspell a key, or use the wrong data type for a specific field.
- Simple regular expression parsing of LLM output is fragile and breaks whenever the model's "voice" or prompt changes slightly.
- Complex nested data structures (e.g., a multi-file refactoring plan or a data migration map) are difficult for an LLM to generate consistently without explicit schema enforcement.
- "Instruction drift": even when told to "output only JSON," an LLM may still add "Here is the JSON you requested:" as a preamble, breaking the parser.

*Yet, solving this problem is feasible because:*

- Most major LLM providers (Anthropic, OpenAI, Google) now support "JSON Mode" or "Tool Use" (Function Calling) which guarantees that the model's output will conform to a specific JSON schema.
- Validation libraries like **Pydantic** (Python) and **Zod** (TypeScript) can be used to define "Gold Standard" schemas that the LLM must follow, with built-in validation and "retry" loops.
- "Constrained decoding" techniques can force a model to only generate tokens that are valid for a specific schema, ensuring 100% syntactic correctness at the token level.

## Solution

Enforce strictly typed schemas on all LLM interactions that serve as input to an automated modernization pipeline:

1. **Define a clear Schema** — Use **Pydantic** or **Zod** to define the exact structure of the output you need (e.g., "A list of files to change, each with a 'path', an 'action' (CREATE/UPDATE/DELETE), and the 'content'").
2. **Use "Tool Use" or "Function Calling"** — Instead of a raw text prompt, define a "tool" that the LLM must call to return its results. The model is then forced by the provider to conform to that tool's schema.
3. **Task the LLM with "Self-Correction"** — If the output fails validation, feed the error message back to the LLM and ask it to fix the JSON. Agents can do this autonomously.
4. **Use "Constrained Decoding" for local models** — If self-hosting, use libraries like **Outlines** or **Guidance** to enforce the schema at the token level, ensuring the output is always valid JSON.
5. **Implement "LLM-as-a-Pipe"** — Treat the LLM call like a standard typed function call in your codebase, ensuring that all inputs and outputs are validated before and after the call.

**Common structured output use cases:**

- **Refactoring Plans** — A structured list of files and changes for an agent to execute.
- **Data Migration Maps** — Mapping legacy columns to modern entity fields.
- **Classification** — Assigning severity, type, and effort scores to technical debt findings.
- **Code Analysis Reports** — Producing a JSON summary of a module's hotspots and dependencies.

## Tradeoffs

**Pros:**

- Turns "unstructured" AI conversations into "structured" software engineering artifacts.
- Enables the building of reliable, multi-step agentic pipelines where the output of one agent is the typed input for the next.
- Dramatically reduces the manual effort of parsing and cleaning up AI-generated text.

**Cons:**

- Strict schemas can sometimes "limit" the LLM's creativity, forcing it to omit useful-but-unexpected information.
- Complex, deeply nested schemas can increase the token count and latency of the LLM call.

**Difficulties:**

- Developing a schema that is flexible enough to handle the "messy" reality of legacy code while being strict enough to be useful.
- Handling the case where the LLM is "partially correct"—returning a valid schema that contains incorrect business logic.

## Rationale

Modernization is a "pipelined" activity—it involves taking information from one step (e.g., analysis) and using it in the next (e.g., refactoring). If the output of each step is a conversational "vibe," the pipeline is brittle and prone to failure. Structured LLM output provides the "typed interfaces" of the agentic era—it is the glue that allows us to build complex, reliable modernization systems that combine human expertise with AI speed and scale.

## Known Uses

- [Anthropic — Tool use (function calling)](https://docs.anthropic.com/en/docs/tool-use) — structured output via tools and function calls.
- [Instructor (Python/TypeScript)](https://python.useinstructor.com/) — a popular library that wraps LLM calls with Pydantic/Zod validation and automatic retries.
- [Outlines](https://github.com/outlines-dev/outlines) — a library for "constrained decoding" that enforces JSON schemas at the token level.

## References

- [Pydantic](https://docs.pydantic.dev/) — the industry-standard data validation library for Python.
- [Zod](https://zod.dev/) — a TypeScript-first schema declaration and validation library.

## Related Patterns

- [Agentic Coding Workflows](../agentic-coding-workflows/) — structured output is the "communication protocol" between different agents in a workflow.
- [AI-driven Technical Debt Detection](../ai-technical-debt-detection/) — the detection agent produces its report in a structured format for easy import into a backlog.
- [LLM-as-judge Evaluation](../llm-as-judge-evaluation/) — the judge provides its score and reasoning in a structured JSON format for easy analysis.

## What Next

After establishing your first structured output pipeline, implement [LLM-as-judge Evaluation](../llm-as-judge-evaluation/) to automatically score the quality of the structured data your agents are producing.

## Staging History

**Trial (Feb 2026):** Structured LLM output is being trialed to build reliable, typed modernization pipelines. Using JSON Mode and Tool Use to enforce schemas is proving essential for integrating agents into traditional software engineering workflows, but teams are still tuning schema flexibility.
