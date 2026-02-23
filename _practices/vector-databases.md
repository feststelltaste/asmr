---
title: "Vector Databases"
stage: apply
category: AI Tooling Setup
description: "Pgvector, Qdrant, Pinecone — semantic search stores used by RAG pipelines. Mature enough to pick based on your existing infrastructure."
strategic_value: supporting
devops_phases: [build, operate]
---

## Overview

Vector databases store high-dimensional embeddings and support fast approximate nearest-neighbor (ANN) search. They are the retrieval backbone of RAG systems.

## Options

| Option | Best For |
|--------|----------|
| **pgvector** | Teams already on PostgreSQL — zero new infra |
| **Qdrant** | Self-hosted, production-grade, rich filtering |
| **Weaviate** | Multi-modal, GraphQL interface |
| **Pinecone** | Managed, serverless, minimal ops overhead |
| **ChromaDB** | Local development and prototyping |
| **Redis** | Already using Redis; low-latency requirement |

## Recommendation

Start with **pgvector** if you use PostgreSQL — you get semantic search without adding a new system to operate. Move to a dedicated vector store only when you need features pgvector doesn't provide (scale, filtering, multi-tenancy).

## Risks & Considerations

- Vector indexes (HNSW, IVFFlat) trade accuracy for speed — tune recall/precision for your use case
- Embedding model changes invalidate stored vectors — plan for re-indexing
- Managed services add cost; self-hosting adds operational burden

## Resources

- [pgvector — vector extension for PostgreSQL](https://github.com/pgvector/pgvector) — simplest starting point for most teams
- [Qdrant documentation](https://qdrant.tech/documentation/) — self-hosted vector search engine
- [Pinecone — managed vector database](https://www.pinecone.io/learn/) — learning resources from Pinecone
- [YouTube — Vector databases explained](https://www.youtube.com/results?search_query=vector+database+comparison+pgvector+qdrant+pinecone+2025)
