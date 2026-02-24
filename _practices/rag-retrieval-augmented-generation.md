---
title: "RAG (Retrieval-Augmented Generation)"
stage: apply
category: AI Tooling Setup
description: "Grounding LLM responses in your own knowledge base via vector search. Essential for AI tools that need to work with internal documentation or codebases."
strategic_value: supporting
devops_phases: [code, operate]
---

# RAG (Retrieval-Augmented Generation)

## Problem

How do you ground an LLM's general-purpose training knowledge in the specific, proprietary facts of your legacy codebase, documentation, and history without the high cost and complexity of fine-tuning?

*This problem is difficult because:*

- LLMs are "frozen in time"—they only know what was in their training data and have no knowledge of your internal APIs, private documentation, or the "why" behind your specific legacy decisions.
- Modernization requires "deep context"—an agent needs to see the specific 10 lines of code it is modifying, plus the 5 related files, the architectural ADR, and the relevant Jira ticket.
- Fitting an entire multi-million line codebase into a single LLM context window is often impossible, even with the latest frontier models, and can lead to "context dilution" where the model loses focus.
- Static documentation is often out of sync with the actual code, leading the AI to make incorrect assumptions if it only relies on its generic training data.

*Yet, solving this problem is feasible because:*

- Retrieval-Augmented Generation (RAG) allows an agent to dynamically "pull in" only the most relevant snippets of code and documentation for the task at hand, just before generating a response.
- Vector search and embeddings make it possible to perform "semantic search" across a massive codebase, finding relevant context even if the keywords do not match exactly.
- RAG provides an "evidence-backed" workflow where the AI can cite the specific files or documents it used to reach its conclusion, making it easier for humans to verify.

## Solution

Implement a RAG pipeline to provide your AI agents with a "live" library of your organization's technical knowledge:

1. **Ingest the knowledge base** — Collect all relevant data sources: source code, documentation (Markdown, PDF), Jira tickets, Slack logs, and architecture decision records (ADRs).
2. **Chunk and Embed** — Split the documents into small, meaningful "chunks" (e.g., individual functions or paragraphs) and convert them into mathematical vectors using an embedding model.
3. **Store in a Vector Database** — Use a specialized store (see **Vector Databases**) to index these vectors for fast semantic search.
4. **Retrieve on Query** — When a developer or agent asks a question, use the query to find the "Top-K" most similar chunks from the vector store.
5. **Augment the Prompt** — Inject these retrieved chunks into the LLM's context window alongside the original query to "ground" its response in your specific data.

**RAG use cases in modernization:**

- **Codebase Q&A** — "Where is the payment processing logic located, and how does it handle currency conversion?"
- **Documentation Assistant** — "What is our established pattern for error handling in the new Go microservices?"
- **Impact Analysis** — "Show me all files that mention the 'UserAccount' table schema."
- **Onboarding** — "Explain the high-level architecture of the legacy monolith based on the available ADRs."

## Tradeoffs

**Pros:**

- Ensures that AI responses are grounded in your actual, private data rather than generic training knowledge.
- Significantly cheaper and more flexible than fine-tuning; the "knowledge base" can be updated in real-time as the code changes.
- Provides a clear "citation trail" for the AI's answers, improving auditability and trust.

**Cons:**

- Retrieval quality depends heavily on the "chunking" and "embedding" strategy—if the retrieval step fails, the AI's answer will be wrong.
- Does not capture "structural" relationships (e.g., dependency graphs) as well as **Knowledge Graph-Augmented Generation (GraphRAG)**.

**Difficulties:**

- Keeping the vector index in sync with a rapidly changing codebase (requires a "re-indexing" pipeline on every commit).
- Balancing the amount of retrieved context to avoid overwhelming the LLM or exceeding the context window.

## Rationale

Modernization is an information-intensive activity. Developers spend 80% of their time searching for information and only 20% writing code. RAG automates the "search" phase, providing the AI agent with exactly the information it needs to be an effective partner in the modernization journey. It turns a "generic" LLM into a "project-specific" expert that knows your codebase as well as (or better than) any single human developer.

## Known Uses

- [Sourcegraph](https://sourcegraph.com/) — uses RAG to provide codebase-wide search and AI assistance for large-scale enterprise projects.
- [GitHub Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — uses RAG to retrieve context from the currently open files and project structure.
- [LlamaIndex](https://docs.llamaindex.ai/) — a popular open-source framework specifically designed for building RAG applications and connecting LLMs to private data.

## References

- [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — an advanced approach to RAG that improves retrieval accuracy by providing more context during the embedding step.
- [LangChain — RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/) — a comprehensive guide to implementing the standard RAG pattern.

## Related Patterns

- [Vector Databases](vector-databases.md) — the underlying storage technology for RAG systems.
- [Knowledge Graph-Augmented Generation (GraphRAG)](knowledge-graph-augmented-generation.md) — the "structural" evolution of RAG that captures deeper relationships.
- [AI-assisted Legacy Code Reading](ai-assisted-legacy-code-reading.md) — RAG provides the "snippets" that the code reading agent uses to build its understanding.

## What Next

After establishing a basic RAG system for your documentation, apply [Knowledge Graph-Augmented Generation (GraphRAG)](knowledge-graph-augmented-generation.md) to capture the deeper, structural dependencies of your codebase.

## Staging History

**Apply (Feb 2026):** Retrieval-Augmented Generation (RAG) is a foundational, well-proven practice for grounding AI agents in proprietary codebase facts. It is a standard requirement for any modernization effort, providing a low-cost and highly flexible alternative to fine-tuning for maintaining up-to-date context.
