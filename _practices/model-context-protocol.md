---
title: "Model Context Protocol (MCP)"
stage: trial
category: LLM Infrastructure
description: "Anthropic's open standard for connecting AI agents to external tools, data sources, and APIs. Rapidly gaining adoption across major IDEs and platforms."
---

## Overview

MCP defines a standard protocol for LLM hosts (Claude, VS Code, Cursor, etc.) to connect to MCP servers — lightweight services that expose tools, resources, and prompts to AI agents. Instead of custom integrations per tool, one MCP server works with any MCP-compatible host.

## Architecture

```
MCP Host (Claude / IDE) ←→ MCP Server ←→ External Tool / API / DB
```

## Why It Matters for Modernization

- Connect AI agents to your legacy systems via MCP servers without changing the legacy code
- Build an MCP server that exposes your internal documentation, JIRA, databases
- Enables AI coding assistants to have live access to your systems during sessions

## Ecosystem (growing rapidly)

- **Official servers**: filesystem, git, databases, web search, browser
- **IDE support**: Claude Desktop, Cursor, Zed, VS Code (Copilot)
- **Community servers**: JIRA, Confluence, GitHub, Slack, PostgreSQL, and many more

## Risks & Considerations

- Protocol is relatively new (late 2024) — breaking changes possible
- Security: MCP servers have access to tools on your behalf — scope permissions carefully
- Tool proliferation: too many tools confuse agents; curate carefully
