---
title: "LLM-driven COBOL Migration"
stage: trial
category: Legacy Modernization
description: "Using LLMs to translate COBOL/RPG/PL1 to modern languages (Java, Kotlin, Python). Requires extensive testing but is now viable for structured batch programs."
---

## Overview

Translating COBOL to a modern language has historically required expensive specialists. LLMs are now capable of producing readable, semantically equivalent code for well-structured COBOL programs — particularly batch processing and report generation routines.

## Approaches

1. **Direct translation** — LLM translates COBOL to Java/Kotlin/Python line-by-line
2. **Semantic rewrite** — LLM understands intent and rewrites in idiomatic modern style
3. **Test-first migration** — Generate characterization tests, then translate, then verify
4. **Hybrid** — Translate core logic; rewrite UI/integration layers from scratch

## Tooling

- **AWS Mainframe Modernization** — Automated COBOL-to-Java translation service
- **IBM watsonx Code Assistant** — LLM-assisted COBOL modernization
- Custom prompting with Claude/GPT-4 for smaller, isolated programs

## Risks & Considerations

- Numeric precision: COBOL's COMP-3 and decimal arithmetic differ from IEEE floats
- COBOL copybooks (shared data definitions) require careful mapping
- Transaction/rollback semantics differ across runtimes
- Always verify with characterization tests capturing production-realistic inputs
