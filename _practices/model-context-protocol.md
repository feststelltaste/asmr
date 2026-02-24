---
title: "Model Context Protocol (MCP)"
stage: apply
category: AI Tooling Setup
description: "Anthropic's open standard for connecting AI agents to external tools, data sources, and APIs. Rapidly gaining adoption across major IDEs and platforms."
strategic_value: supporting
devops_phases: [code, build]
---

# Model Context Protocol (MCP)

## Problem

How do you efficiently and securely connect multiple AI agents to a wide variety of external tools, data sources, and proprietary legacy systems without building custom, brittle integrations for every single combination of agent and tool?

*This problem is difficult because:*

- Each AI agent or IDE (Claude Desktop, VS Code, Cursor, Zed) traditionally has its own proprietary way of connecting to external "tools" (e.g., shell, database, Jira, web search).
- Building a custom "tool connector" for a proprietary legacy system (like an old mainframe or a custom internal API) is a major engineering effort that must be repeated for every agent or IDE.
- Sharing "context" (e.g., the current file, the database schema, the recent git commits) across different agents and tools is inconsistent and error-prone.
- Security and permission management for agent "tool use" is difficult to centralize and audit when each tool uses a different proprietary protocol.
- The "N x M" problem: if you have N agents and M tools, you traditionally need N x M integrations to connect them all.

*Yet, solving this problem is feasible because:*

- Anthropic's **Model Context Protocol (MCP)** provides an open, standard way for LLM "hosts" (like Claude Desktop or an IDE) to connect to MCP "servers" that expose tools, resources, and prompts.
- One MCP server can be used by *any* MCP-compatible host, making tool integrations reusable across the entire agentic ecosystem.
- MCP servers can be lightweight, self-hosted services that wrap proprietary legacy systems and expose them safely to AI agents via a standard JSON-RPC protocol.
- The rapidly growing ecosystem of open-source MCP servers (for GitHub, Slack, Postgres, Jira) provides an "off-the-shelf" foundation for any modernization effort.

## Solution

Utilize the Model Context Protocol to create a unified "tool and context" layer for all your AI agents:

1. **Deploy standard MCP servers** — Use existing, open-source MCP servers to connect your agents to common tools like **GitHub**, **Jira**, **PostgreSQL**, and the local **Filesystem**.
2. **Build custom MCP servers for legacy systems** — Wrap your proprietary legacy APIs or databases in a simple MCP server that exposes specific tools (e.g., `query_legacy_db`, `read_mainframe_log`) to the AI agents.
3. **Configure MCP Hosts** — Connect your preferred agentic tools (like Claude Desktop or Cursor) to your MCP servers using their native configuration (e.g., `claude_desktop_config.json`).
4. **Curate the "Tool Set"** — Instead of giving agents unlimited access, curate a specific set of MCP tools for each modernization task to prevent "tool confusion" and reduce costs.
5. **Enforce Security and Permissions** — Use the MCP server as a "security gateway" to log, audit, and strictly control the actions an AI agent can take on your legacy systems.

**MCP Core Primitives:**

- **Tools** — Functions that an LLM can call to perform actions (e.g., "Write this file," "Run this SQL query").
- **Resources** — Data sources that an LLM can read as context (e.g., "The database schema," "A specific Jira ticket").
- **Prompts** — Pre-defined "templates" for specific interactions (e.g., "Explain this legacy module").

## Tradeoffs

**Pros:**

- Solves the "N x M" integration problem: build a tool connector once and use it with any MCP-compatible agent or IDE.
- Simplifies the process of giving AI agents "eyes and hands" in your unique legacy environment.
- Provides a standard, auditable protocol for all agentic tool interactions.

**Cons:**

- The protocol is relatively new (late 2024), and breaking changes in the specification are still possible.
- If an MCP server is compromised, an attacker could potentially use the exposed tools to gain unauthorized access to your systems.

**Difficulties:**

- Ensuring that the "tool descriptions" in the MCP server are precise enough for the LLM to understand how and when to use them correctly.
- Managing the lifecycle and configuration of many different MCP servers across a large development team.

## Rationale

Modernization agents are only as powerful as the tools they can use. If an agent is "trapped" in a chat window without access to your code, your Jira tickets, or your database, its value is severely limited. MCP provides the "plug-and-play" infrastructure for the agentic era—it is the USB port for LLMs. By adopting a standard protocol for tool and context integration, teams can build a rich, reusable "modernization toolbox" that powers any agentic tool they choose to use, now and in the future.

## Known Uses

- [Anthropic — MCP documentation](https://docs.anthropic.com/en/docs/mcp) — the official specification and getting-started guide for the protocol.
- [MCP servers registry](https://github.com/modelcontextprotocol/servers) — a centralized repository of open-source MCP servers for many popular tools and platforms.
- [Claude Desktop](https://claude.ai/download) — the first major LLM host to fully support MCP for connecting to local and remote tools.
- [Cursor IDE](https://cursor.com/) — a popular AI-native IDE that uses MCP to extend its capabilities.

## References

- [Model Context Protocol (MCP) — Introduction Video](https://www.youtube.com/watch?v=CQywdSdi5iA) — a high-level overview of the protocol and its benefits.
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification) — the underlying transport protocol used by MCP.

## Related Patterns

- [Agentic Coding Workflows](../agentic-coding-workflows/) — MCP provides the "tool and context" layer that makes these workflows possible.
- [Legacy Knowledge Recovery Agents](../legacy-knowledge-recovery-agents/) — discovery agents use MCP servers to query Jira, Slack, and old documentation.
- [Agent Sandboxing](../agent-sandboxing/) — MCP servers that run local tools must be sandboxed to ensure they don't have unauthorized access to the host system.

## What Next

After connecting your first standard MCP server (like GitHub or Filesystem), build a simple **custom MCP server** that exposes a single, high-value legacy data source (like a database schema or an internal API) to your agents.

## Staging History

**Apply (Feb 2026):** The Model Context Protocol (MCP) has rapidly become the standard for connecting AI agents to legacy tools and data sources. Its ability to provide a unified, reusable integration layer has made it a proven choice for scaling agentic modernization across diverse enterprise environments.
