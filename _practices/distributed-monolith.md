---
title: "Monolith (Distributed)"
stage: stop
category: Architecture & Delivery
description: "Tightly coupled services that must deploy together — worst of both worlds. Do not build new distributed systems this way."
strategic_value: generic
devops_phases: [plan, deploy]
---

## Why Stop

A distributed monolith looks like microservices but behaves like a monolith: services are physically separate but share databases, deploy in lockstep, or make synchronous calls in long dependency chains. You pay the operational cost of distributed systems without getting the independence benefits.

## Common Symptoms

- Services that can only be deployed in a specific order
- Shared database tables accessed by multiple services
- Cascading failures when one service is slow or down
- Changes to one service requiring changes in multiple others

## How It Happens

- Microservices created by splitting the deployment unit but not the data or logic
- Shared libraries that change frequently and require coordinated updates
- Synchronous call chains: Service A → B → C → D (one failure brings all down)

## What to Do Instead

- Identify true bounded contexts before splitting — see [Domain-Driven Refactoring](/practices/domain-driven-refactoring/)
- Own your data — see [Database Decomposition](/practices/database-decomposition/)
- Prefer async event communication for cross-service coordination
- If you can't deploy a service independently, it's not a microservice

## Resources

- [Sam Newman — Monolith to Microservices](https://www.oreilly.com/library/view/monolith-to-microservices/9781492047834/) — patterns for avoiding and resolving distributed monolith problems
- [Martin Fowler — Microservices prerequisites](https://martinfowler.com/bliki/MicroservicePrerequisites.html) — what you need before going microservices
- [YouTube — Distributed monolith anti-pattern](https://www.youtube.com/results?search_query=distributed+monolith+anti+pattern+microservices+2025)
