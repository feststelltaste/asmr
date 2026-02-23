---
title: "Structured LLM Output (JSON mode)"
stage: apply
category: AI Tooling Setup
description: "Enforcing typed JSON schemas on LLM output (tool use, JSON mode). Makes LLMs reliable participants in typed software pipelines."
strategic_value: generic
devops_phases: [code, build]
---

## Overview

Unstructured text output from LLMs is hard to integrate into software pipelines. Structured output — enforced JSON matching a schema — makes LLM calls behave like typed function calls, enabling reliable parsing and downstream processing.

## Approaches

- **Tool use / function calling** — Provider guarantees schema-conformant output (Anthropic, OpenAI, Gemini)
- **JSON mode** — Forces valid JSON without a schema (less strict)
- **Constrained decoding** — Libraries like `outlines`, `guidance` enforce schemas at token level
- **Pydantic + instructor** — Python library wrapping LLM calls with Pydantic model validation and retry

## Use Cases

- Extracting structured data from legacy documentation
- Generating migration scripts in a structured format for review
- Producing typed diffs/patches that can be applied programmatically
- Classifying code into categories (e.g., assigning technologies to roadmap stages)

## Risks & Considerations

- Tool use / JSON mode increases token count slightly
- Complex nested schemas may hit model capability limits
- Always validate output against schema even when using JSON mode — providers can still make mistakes

## Resources

- [Anthropic — Tool use (function calling)](https://docs.anthropic.com/en/docs/tool-use) — structured output via tools
- [instructor — Python library for structured outputs](https://python.useinstructor.com/) — Pydantic-validated LLM responses
- [outlines — constrained text generation](https://github.com/outlines-dev/outlines) — token-level schema enforcement
