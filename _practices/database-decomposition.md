---
title: "Database Decomposition"
stage: trial
category: Legacy Modernization
description: "Breaking apart a shared monolithic DB into service-owned schemas or separate databases. Hard but critical for enabling independent deployment."
strategic_value: supporting
devops_phases: [plan, code, deploy, operate]
---

## Overview

A shared monolithic database is often the biggest coupling point in a legacy system. Decomposing it into service-owned data stores unlocks independent deployability, technology choice per service, and team autonomy.

## Stages

1. **Identify bounded contexts** — Which tables logically belong to which domain?
2. **Separate schemas** — Move tables into per-service schemas within the same DB
3. **Introduce APIs** — Replace cross-service DB joins with service-to-service API calls
4. **Split databases** — Move schemas into physically separate databases
5. **Migrate data** — Use dual-write or staged synchronization to migrate data with zero downtime

## AI Acceleration

- LLMs can analyze SQL queries across the codebase to map table ownership
- Identify which services read/write which tables via query pattern analysis
- Generate data migration scripts and integration tests

## Risks & Considerations

- Cross-service queries become network calls — latency and failure modes change
- Distributed transactions are hard; prefer eventual consistency where possible
- Data consistency is the primary risk — move incrementally with extensive testing

## Resources

- [Sam Newman — Monolith to Microservices](https://www.oreilly.com/library/view/monolith-to-microservices/9781492047834/) — dedicated chapters on database decomposition patterns
- [Martin Fowler — Database Decomposition patterns](https://martinfowler.com/articles/patterns-of-distributed-systems/) — patterns for distributed data
- [Flyway / Liquibase](https://flywaydb.org/) — schema migration tools for incremental DB changes
