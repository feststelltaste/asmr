---
title: "Manual Server Provisioning"
stage: remove
category: Architecture & Delivery
description: "Hand-configuring servers without IaC. Impossible to review, reproduce, or hand off to an AI agent safely."
---

## Why Remove

Servers configured by hand accumulate undocumented changes ("snowflakes"). Provisioning cannot be reviewed, versioned, or reproduced. When the server fails, recovery depends on institutional memory. No AI agent can participate in or verify a manual provisioning process.

## Migration Path

1. Document what's on existing servers (use LLMs to help read shell history and config files)
2. Express current state as [Infrastructure as Code](/technologies/infrastructure-as-code/)
3. Provision new servers using IaC; migrate workloads
4. Decommission hand-provisioned servers

## Tooling for Migration

- **Ansible** — Convert existing bash setup scripts to idempotent playbooks as a stepping stone
- **Terraform** — Declare compute and network resources
- **Packer** — Build machine images with all dependencies baked in
- **Cloud-init** — Minimal bootstrapping to pull configuration from IaC

## Risks of Keeping It

- Disaster recovery is slow and unreliable
- Security patches are applied inconsistently
- Impossible to scale or reproduce environments for testing
