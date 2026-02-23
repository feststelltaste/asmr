---
title: "Automated Dead Code Removal"
stage: trial
category: Legacy Modernization
description: "AI and static analysis tooling to detect and safely remove unused code paths, dead features, and unreachable branches in large legacy systems."
strategic_value: supporting
devops_phases: [code, build]
---

## Overview

Large legacy codebases accumulate dead code — unused methods, unreachable branches, disabled features, old API versions — that makes the system harder to understand and modify. AI tools combined with static analysis can identify and safely remove this clutter at scale.

## Tooling

- **Static analysis** — SonarQube, Semgrep, language-specific tools (e.g., `jdepend`, `vulture`)
- **Coverage-guided** — Identify code paths never exercised in production
- **LLM-assisted** — Ask LLM to confirm whether a function appears truly unused given codebase context
- **Feature flag audits** — Find flags permanently enabled/disabled and inline their branches

## Process

1. Run static analysis to get dead code candidates
2. Cross-reference with production coverage data
3. Use LLM to verify: "Is this function called anywhere, including dynamically?"
4. Generate a PR removing each candidate; run full test suite

## Risks & Considerations

- Reflection, serialization, and dynamic dispatch hide real usages from static analysis
- Some "dead" code may be intentional — error handlers, backwards compatibility stubs
- Move slowly: remove in small batches, deploy, monitor before removing more

## Resources

- [SonarQube — static analysis](https://www.sonarsource.com/products/sonarqube/) — industry-standard dead code and quality detection
- [Semgrep — static analysis for custom rules](https://semgrep.dev/) — write rules to detect project-specific dead code patterns
- [vulture — Python dead code detection](https://github.com/jendrikseipp/vulture) — simple Python dead code finder
- [YouTube — Finding and removing dead code with AI](https://www.youtube.com/results?search_query=dead+code+removal+static+analysis+ai+2025)
