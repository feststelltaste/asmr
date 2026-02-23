---
title: "Knowledge Graph-Augmented Generation (GraphRAG)"
stage: trial
category: AI Tooling Setup
description: "Combining vector search with structured graph databases to help agents navigate complex codebase dependencies and domain relationships."
strategic_value: supporting
devops_phases: [plan, code]
---

## Overview

Traditional RAG (vector search) excels at finding "similar" text chunks but struggles with "structural" questions like *'Which services depend on this database column?'* or *'What is the full business process for processing an invoice?'*. 

Knowledge Graph-Augmented Generation (GraphRAG) maps the entities in your system (classes, tables, Jira tickets, developers) and their relationships into a traversable graph. This provides AI agents with a high-fidelity map of the system, enabling deeper reasoning and better impact analysis during modernization.

## Why It Matters for Modernization

- **Impact Analysis** — Agents can traverse the graph to see the ripple effects of a proposed refactoring across multiple services.
- **Context Stitching** — Connects code to non-code context (e.g., *'This class implements the business rule defined in Ticket-402'*).
- **Global Understanding** — Better than simple chunking for summarizing the behavior of large, multi-file modules.

## How It Works

1. **Extraction** — An LLM or static analyzer identifies entities and relationships from the codebase and documentation.
2. **Graph Construction** — These are stored in a graph database (Neo4j, FalkorDB).
3. **Retrieval** — When an agent asks a question, the system retrieves relevant graph nodes and their neighbours, providing a "neighborhood" of context.
4. **Synthesis** — The LLM uses both the graph structure and the text content to generate an answer.

## Tools

- **Microsoft GraphRAG** — Open-source library for building graph-based RAG.
- **Neo4j** — Industry-standard graph database with built-in vector support.
- **FalkorDB** — High-performance graph database optimized for LLMs.
- **LlamaIndex PropertyGraph** — Framework for easily building knowledge graphs from documents.

## Resources

- [Microsoft Research — GraphRAG: Unlocking LLM discovery on narrative private data](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)
- [Neo4j — Knowledge Graphs for LLMs](https://neo4j.com/generative-ai/)
- [LlamaIndex — Property Graph Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/)
