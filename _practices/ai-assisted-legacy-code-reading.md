---
title: "AI-assisted Legacy Code Reading"
stage: apply
category: Legacy Modernization
description: "Using LLMs to explain, document, and map unknown legacy code — COBOL, old Java, undocumented PHP. Dramatically reduces the 'understanding' phase."
strategic_value: core
devops_phases: [plan, code]
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

- Use models with massive context windows (Gemini 1.5 Pro, Claude 3.5 Sonnet) to read entire modules or small codebases at once
- For very large monoliths, break context by bounded context or module to improve reasoning quality
- Ask the LLM to generate a glossary of domain terms it finds in the code

## Risks & Considerations

- LLMs can misread ambiguous logic — always verify against tests or SME knowledge
- Very old languages (COBOL, PL/1, RPG) have less training data; results vary
- Don't trust the LLM's summary of security-critical code without manual review

## Resources

- [Sourcegraph — code intelligence for large codebases](https://sourcegraph.com/) — search and understand code at scale
- [GitHub Copilot Chat — explain code feature](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — ask questions about any code in the IDE
- [YouTube — Using AI to understand legacy code](https://www.youtube.com/results?search_query=ai+llm+understand+explain+legacy+code+2025)
- [YouTube — Reading COBOL with AI assistance](https://www.youtube.com/results?search_query=ai+read+cobol+legacy+code+llm+2025)
