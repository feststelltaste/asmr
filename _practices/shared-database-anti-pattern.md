---
title: "Shared Database Anti-pattern"
stage: remove
category: Legacy Modernization
description: "Multiple services or teams sharing one database schema without boundaries. Creates hidden coupling that makes independent deployment impossible."
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

- [Database Decomposition](/technologies/database-decomposition/)
- [Domain-Driven Refactoring](/technologies/domain-driven-refactoring/)
