---
title: "Shared Database Anti-pattern"
stage: remove
category: Legacy Modernization
description: "Multiple services or teams sharing one database schema without boundaries. Creates hidden coupling that makes independent deployment impossible."
strategic_value: generic
devops_phases: [deploy, operate]
---

## Why Remove

Shared databases create invisible contracts between teams. Any schema change risks breaking other services. Deployments must be coordinated. There is no way to independently scale, replace, or optimize a service's data store. This is one of the main reasons microservice migrations fail — teams moved to separate services but kept the shared database.

## Migration Path

1. Map which tables each service owns vs. reads
2. For tables with multiple writers, designate a single owning service
3. Replace cross-service DB access with API calls (read) or domain events (write-propagation)
4. Move to separate schemas per service in the same DB cluster
5. Eventually split into physically separate databases when the team/scale justifies it

## See Also

- [Database Decomposition](/practices/database-decomposition/)
- [Domain-Driven Refactoring](/practices/domain-driven-refactoring/)

## Resources

- [Sam Newman — Monolith to Microservices](https://www.oreilly.com/library/view/monolith-to-microservices/9781492047834/) — definitive guide to database ownership patterns
- [Martin Fowler — Integration Database](https://martinfowler.com/bliki/IntegrationDatabase.html) — why shared databases cause problems
- [YouTube — Shared database anti-pattern explained](https://www.youtube.com/results?search_query=shared+database+anti+pattern+microservices+2025)
