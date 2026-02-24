---
title: "Vector Databases"
stage: apply
category: AI Tooling Setup
description: "Pgvector, Qdrant, Pinecone — semantic search stores used by RAG pipelines. Mature enough to pick based on your existing infrastructure."
strategic_value: supporting
devops_phases: [build, operate]
---

# Vector Databases

## Problem

How do you efficiently store and retrieve the millions of high-dimensional "embeddings" needed to power semantic search and RAG (Retrieval-Augmented Generation) for a massive, complex legacy codebase?

*This problem is difficult because:*

- Traditional relational databases (like standard PostgreSQL or MySQL) are not optimized for "vector similarity search," making it slow and inefficient to find relevant code snippets across a million files.
- High-dimensional vectors (often 1536+ dimensions) require specialized indexing structures (like HNSW or IVFFlat) to achieve fast "approximate nearest neighbor" (ANN) search at scale.
- Keeping a vector index in sync with a rapidly changing codebase is a significant operational burden: any code change requires a "re-embedding" and "re-indexing" step.
- Selecting the "right" vector database is a complex decision: should you use a managed cloud service (Pinecone), an open-source dedicated store (Qdrant, Weaviate), or an extension to your existing database (pgvector)?

*Yet, solving this problem is feasible because:*

- **pgvector** provides a high-performance vector extension for PostgreSQL, allowing teams to store and query embeddings without adding a new, specialized system to their operational stack.
- Dedicated vector databases (Qdrant, Pinecone, Weaviate) offer advanced features like multi-tenancy, complex filtering, and massive-scale indexing for the most demanding RAG pipelines.
- Modern vector stores can perform billions of similarity searches in milliseconds, providing the "real-time" performance needed for interactive AI coding assistants and agentic workflows.
- Vector search is now "commoditized"—you can pick a store based on your existing infrastructure and team expertise rather than just raw performance.

## Solution

Deploy a vector database as the retrieval engine for your modernization project's RAG and semantic search pipelines:

1. **Pick a database based on your "infrastructure first"** — Use **pgvector** if you are already on PostgreSQL; use **Qdrant** or **Weaviate** if you need a dedicated, open-source store; or use **Pinecone** if you want a managed, "serverless" experience.
2. **Implement an "Embedding Pipeline"** — Create a service that automatically "chunks" your code and documentation and sends it to an embedding model (like OpenAI `text-embedding-3`) before storing it in the vector database.
3. **Configure Vector Indexing** — Select an index type (like HNSW) that balances "recall" (accuracy) and "latency" (speed) for your specific use case.
4. **Enable Metadata Filtering** — Store metadata alongside your vectors (e.g., `file_path`, `author`, `last_modified`) so you can "filter" your search results (e.g., "Find code similar to this, but only in the `billing` module").
5. **Establish a "Re-indexing" Strategy** — Connect your vector store to your CI/CD pipeline to ensure that any code changes are automatically reflected in the index.

**Common Vector Database options:**

- **pgvector** — A vector extension for PostgreSQL; the simplest starting point for most teams.
- **Qdrant** — A high-performance, open-source vector search engine written in Rust.
- **Weaviate** — An open-source vector database that includes built-in support for multi-modal search and a GraphQL interface.
- **Pinecone** — A managed, cloud-native vector database that is optimized for scale and minimal operational overhead.
- **ChromaDB** — An open-source, "lightweight" vector store that is popular for local development and prototyping.

## Tradeoffs

**Pros:**

- Enables "semantic search" that can find relevant context even if keywords don't match.
- Dramatically faster and more efficient than traditional full-text search for large-scale AI applications.
- Provides a centralized "memory" for all your AI agents to share across many sessions.

**Cons:**

- Adds an additional system to your operational stack (unless using pgvector).
- "Approximate" search means you might occasionally miss the most relevant result or get a "plausible but irrelevant" one.
- Changing your embedding model requires a full "re-indexing" of all your stored vectors.

**Difficulties:**

- Tuning the "chunking" and "embedding" strategy to ensure that the search results are actually useful for the AI.
- Balancing the cost of managed vector services with the operational burden of self-hosting a dedicated store.

## Rationale

Vector search is the "search engine" of the agentic era. Without it, an AI agent is limited to the few files it can see in its immediate context. A vector database provides the "global memory" that allows an agent to navigate millions of lines of code and documentation with ease. By picking a store that fits your existing infrastructure, you can build a powerful RAG pipeline with minimal risk and maximum performance for your modernization journey.

## Known Uses

- [pgvector](https://github.com/pgvector/pgvector) — the most popular way to add vector search to an existing PostgreSQL database.
- [Qdrant](https://qdrant.tech/) — used by many AI-native companies for its high performance and rich filtering capabilities.
- [Pinecone](https://www.pinecone.io/) — used by teams that want a managed, high-scale vector store without any operational overhead.

## References

- [Vector Databases — A Comprehensive Guide](https://www.pinecone.io/learn/vector-database/) — a deep dive into how vector databases work and why they are needed for LLM applications.
- [pgvector — GitHub](https://github.com/pgvector/pgvector) — documentation and source code for the PostgreSQL vector extension.

## Related Patterns

- [RAG (Retrieval-Augmented Generation)](../rag-retrieval-augmented-generation/) — vector databases are the primary storage and retrieval engine for RAG.
- [Knowledge Graph-Augmented Generation (GraphRAG)](../knowledge-graph-augmented-generation/) — GraphRAG combines vector search with a graph database for even richer context.
- [AI-assisted Codebase Analytics](../ai-assisted-codebase-analytics/) — vector search can be used to find "duplicate" or "similar" logic across a massive codebase.

## What Next

After establishing your first vector store (like [pgvector](https://github.com/pgvector/pgvector)), implement a [RAG (Retrieval-Augmented Generation)](../rag-retrieval-augmented-generation/) pipeline to provide your agents with live access to your code and documentation.

## Staging History

**Apply (Feb 2026):** Vector databases are a mature and foundational part of the 'AI stack'. Every team building agentic tools or RAG pipelines has a vector store in place, with pgvector being the most popular choice for teams already using PostgreSQL.
