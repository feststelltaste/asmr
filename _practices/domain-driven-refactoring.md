---
title: "Domain-Driven Refactoring"
stage: apply
category: Legacy Modernization
description: "Using DDD techniques (bounded contexts, ubiquitous language) to find the right cuts when splitting a monolith. LLMs can help identify domain concepts in code."
strategic_value: supporting
devops_phases: [plan, code]
---

## Overview

DDD provides the vocabulary and patterns (bounded contexts, aggregates, domain events, ubiquitous language) to identify where a monolith should be split. The key insight is that organizational boundaries and domain boundaries should align. LLMs make this discovery phase faster.

## AI-assisted Discovery

- Ask an LLM to identify domain concepts and entity names from the codebase
- Map which modules share the same concepts under different names (semantic overlap)
- Generate a context map draft from existing code structure and dependencies
- Identify aggregate roots by analyzing transaction boundaries

## Key DDD Patterns for Modernization

- **Bounded Context** — Clear ownership boundary; basis for a microservice
- **Context Map** — Documents how contexts relate and integrate
- **Ubiquitous Language** — Shared vocabulary between code and business — clarify it now
- **Domain Events** — Events that cross context boundaries; basis for async integration

## Risks & Considerations

- Domain modeling requires domain expert involvement — don't let LLMs drive this alone
- Over-engineering into too many tiny contexts creates distributed monolith problems
- The refactoring must be incremental; a full DDD rewrite is a big-bang rewrite

## Resources

- [Eric Evans — Domain-Driven Design (Blue Book)](https://www.domainlanguage.com/ddd/) — foundational DDD concepts including bounded contexts
- [Vaughn Vernon — Implementing Domain-Driven Design](https://vaughnvernon.com/?page_id=168) — hands-on patterns for applying DDD
- [EventStorming by Alberto Brandolini](https://www.eventstorming.com/) — collaborative technique for discovering bounded contexts
- [Henning Schwentner — Domain-Driven Refactorings](https://hschwentner.io/domain-driven-refactorings/) — catalog of DDD-based refactoring patterns
- [YouTube — DDD for legacy modernization](https://www.youtube.com/results?search_query=domain+driven+design+legacy+modernization+bounded+context+2025)
