---
title: "RAG (Retrieval-Augmented Generation)"
stage: apply
category: AI Tooling Setup
description: "Grounding LLM responses in your own knowledge base via vector search. Essential for AI tools that need to work with internal documentation or codebases."
strategic_value: supporting
devops_phases: [code, operate]
---

## Overview

RAG augments an LLM's static training knowledge with dynamic retrieval from your own data: documentation, code, tickets, runbooks, architecture decisions. The retrieval step finds relevant passages, which are injected into the LLM's context before generating a response.

## Architecture

```
Query → Embed → Vector Search → Top-K Chunks → LLM Context → Response
```

## Components

- **Chunking strategy** — How to split documents (fixed-size, semantic, by function)
- **Embedding model** — Converts text to vectors (OpenAI `text-embedding-3`, `nomic-embed-text`, etc.)
- **Vector store** — Stores and retrieves embeddings (see [Vector Databases](/technologies/vector-databases/))
- **LLM** — Synthesizes retrieved context into an answer

## Use Cases in Modernization

- Codebase Q&A: "Where is the payment processing logic?"
- Internal documentation assistant
- Compliance checking against architecture decision records
- Onboarding: ask questions about the system without reading everything

## Risks & Considerations

- Retrieval quality depends heavily on chunking and embedding strategy
- Retrieved context may be outdated if indexing is not kept in sync
- Context window limits how much retrieved content can be used at once

## Resources

- [Anthropic — RAG guide](https://www.anthropic.com/news/contextual-retrieval) — contextual retrieval approach for better RAG
- [LlamaIndex documentation](https://docs.llamaindex.ai/) — comprehensive RAG framework and patterns
- [LangChain RAG tutorial](https://python.langchain.com/docs/tutorials/rag/) — step-by-step RAG implementation
- [YouTube — RAG explained and implemented](https://www.youtube.com/results?search_query=rag+retrieval+augmented+generation+implementation+2025)
