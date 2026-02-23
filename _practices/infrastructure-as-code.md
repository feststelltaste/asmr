---
title: "Infrastructure as Code"
stage: apply
category: Architecture & Delivery
description: "Managing all infra via Terraform, Pulumi, or CDK. Enables AI agents to propose infrastructure changes safely through code review."
---

## Overview

IaC declares infrastructure (networks, compute, databases, permissions) in version-controlled code. Changes go through review, CI validation, and automated apply — making infrastructure reproducible, auditable, and safe to modify.

## Why It Matters for AI-assisted Development

AI agents can now write and modify IaC:
- Propose infra changes as PRs for human review
- Generate Terraform modules for new services
- Migrate legacy CloudFormation to Terraform or Pulumi
- Identify security misconfigurations in existing IaC

## Tools

| Tool | Approach |
|------|----------|
| **Terraform / OpenTofu** | HCL declarative, massive ecosystem |
| **Pulumi** | Real programming languages (TS, Python, Go) |
| **AWS CDK** | TypeScript/Python DSL compiling to CloudFormation |
| **Ansible** | Procedural, good for config management |

## Risks & Considerations

- State management: Terraform state can drift or become corrupted — use remote state with locking
- `terraform destroy` is dangerous — guard against accidental deletion
- IaC does not automatically manage secrets — integrate with Vault or cloud secrets manager
- AI-generated IaC must be reviewed carefully for security and cost implications
