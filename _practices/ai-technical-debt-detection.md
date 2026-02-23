---
title: "AI-driven Technical Debt Detection"
stage: assess
category: Agentic AI Tools
description: "Using LLMs to systematically identify, classify, and prioritize technical debt across a codebase — turning a slow manual process into an automated, prioritized backlog."
strategic_value: core
---

## Overview

Technical debt identification has always been subjective and expensive — it requires experienced engineers to spend time reading code they don't maintain. LLMs can now perform a first pass of this analysis at scale: reading modules, identifying violations of good design, flagging coupling, noting missing tests, and producing structured debt reports.

The goal is not to replace engineering judgment, but to surface issues fast enough that teams can make informed prioritization decisions instead of guessing.

## What AI Can Detect

- **Code smells** — Long methods, excessive coupling, duplicated logic, deep nesting
- **Outdated dependencies** — Libraries with known vulnerabilities or no longer maintained
- **Missing or weak test coverage** — Functions with no tests, tests that only test happy paths
- **Implicit business rules** — Logic embedded in code without documentation or explanation
- **Architectural violations** — Calls that cross bounded context boundaries incorrectly
- **Dead code** — Unreachable paths, unused parameters, stale feature flag branches

## Approach

1. Feed the LLM a module or bounded context at a time
2. Ask for a structured debt report (severity, location, rationale)
3. Use structured output (JSON) to import findings into your issue tracker
4. Cross-reference with production usage data to prioritize what matters most
5. Use the report as a starting point for team discussion, not a definitive list

## Limitations

- LLMs flag potential issues; human judgment is required to confirm and prioritize
- Lacks runtime context — a "dead" function may be called via reflection
- Quality degrades on very large files; chunk by logical unit
- Does not understand *business* value — can't tell you which debt is most dangerous for your domain

## Resources

- [Martin Fowler — Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) — framework for classifying debt types
- [SonarQube](https://www.sonarsource.com/products/sonarqube/) — static analysis to combine with LLM findings
- [YouTube — AI for Technical Debt Detection](https://www.youtube.com/results?search_query=ai+llm+technical+debt+detection+codebase+2025)
