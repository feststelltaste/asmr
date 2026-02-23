---
title: "Event-Driven Architecture"
stage: trial
category: Architecture & Delivery
description: "Async communication via events (Kafka, EventBridge). Decouples legacy systems from new services during modernization."
---

## Overview

In event-driven architecture, services communicate by publishing and consuming events rather than making synchronous API calls. Producers don't know about consumers, enabling loose coupling and independent evolution.

## Value in Modernization

- **Decouple legacy from new** — Legacy system publishes events; new services consume them without changing the legacy system
- **Outbox pattern** — Bridge legacy DB changes to events reliably
- **Parallel operation** — Old and new implementations consume the same events during migration
- **Audit trail** — Events naturally provide an immutable history of what happened

## Tools

- **Apache Kafka** — High-throughput, durable, the standard for large scale
- **AWS EventBridge** — Managed, serverless event bus with routing rules
- **NATS / JetStream** — Lightweight, low-latency messaging
- **RabbitMQ** — Traditional message broker, simpler ops than Kafka

## Risks & Considerations

- Eventual consistency is hard to reason about — design for it explicitly
- Schema evolution needs governance (Confluent Schema Registry or AsyncAPI contracts)
- Debugging distributed event flows requires good observability
- Don't use events for everything — synchronous calls are simpler when real-time response is required
