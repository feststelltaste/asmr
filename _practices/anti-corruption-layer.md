---
title: "Anti-Corruption Layer"
stage: apply
category: Legacy Modernization
description: "A translation layer between legacy concepts and new domain models. Prevents legacy data structures from leaking into freshly written code."
strategic_value: supporting
---

## Overview

When integrating with a legacy system, the ACL translates between the legacy's implicit domain model (often muddled, inconsistent, or technically constrained) and your new system's clean domain model. It isolates the new code from legacy concepts.

## When to Use

- Integrating with a legacy system you don't control or can't change
- When the legacy model uses concepts that conflict with your new domain language
- Protecting new microservices from a shared legacy database schema

## Implementation Patterns

- **Adapter** — Converts legacy DTOs to your domain objects at the boundary
- **Repository** — Hides legacy DB access behind a clean interface
- **Gateway** — Wraps legacy API calls in a typed, domain-friendly client

## AI Acceleration

LLMs are effective at:
- Reading legacy code and generating adapter/mapper classes
- Identifying mismatches between legacy and new domain models
- Suggesting naming for concepts that lack clear names in the legacy system

## Risks & Considerations

- The ACL becomes a maintenance burden if the legacy changes frequently
- Don't allow ACL concepts to bleed into the domain — keep it at the boundary

## Resources

- [Eric Evans — Domain-Driven Design (Blue Book)](https://www.domainlanguage.com/ddd/) — the original DDD book introducing the ACL concept
- [Vaughn Vernon — Implementing Domain-Driven Design](https://vaughnvernon.com/?page_id=168) — practical patterns including ACL implementation
- [YouTube — Anti-Corruption Layer in practice](https://www.youtube.com/results?search_query=anti+corruption+layer+ddd+pattern+2025)
