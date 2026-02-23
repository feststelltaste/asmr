---
title: "AI-assisted Legacy Code Reading"
stage: apply
category: Legacy Modernization
description: "Using LLMs to explain, document, and map unknown legacy code — COBOL, old Java, undocumented PHP. Dramatically reduces the 'understanding' phase."
---

## Overview

One of the biggest costs in legacy modernization is simply *understanding* what the code does. LLMs can read unfamiliar code and produce plain-English explanations, call graphs, data flow descriptions, and summaries — compressing weeks of archaeology into hours.

## Use Cases

- **Explain this function** — What does this 500-line COBOL program do?
- **Map data flows** — Which fields from table X are used in which calculations?
- **Identify business rules** — What validation logic is embedded in this service?
- **Summarize modules** — Give me an architectural overview of this package
- **Find entry points** — Where does user input first touch this system?

## Tips

- Break large files into sections when they exceed context windows
- Use RAG over the whole codebase for cross-file questions
- Ask the LLM to generate a glossary of domain terms it finds in the code

## Risks & Considerations

- LLMs can misread ambiguous logic — always verify against tests or SME knowledge
- Very old languages (COBOL, PL/1, RPG) have less training data; results vary
- Don't trust the LLM's summary of security-critical code without manual review
