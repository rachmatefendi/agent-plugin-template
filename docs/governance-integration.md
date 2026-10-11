# Governance integration design

Use the [optional integration reference](../plugin/references/governance-integration.md) and [adoption profile](../plugin/templates/governance-profile.md) only for relevant engagements. Default to reference-only. This source release adds instruction-level boundaries, not an adopted organizational policy or enforced runtime.

## Source roles

- AFGS: architectural prior work explaining governance jurisdictions and execution eligibility. Its public companions are non-normative.
- MDGR: public normative specification of material-decision outcomes. Explicit scoped adoption is required before claiming compatibility.
- APOS Architecture Deep Research: user-supplied research rationale for a bounded project layer. Treat its ratings as report claims, not empirical results or independent validation.
- Plugin: reusable capabilities and draft findings. It does not acquire decision authority from any of these references.

## State ownership

Before integrating APOS with AI Founder OS, name one authoritative owner/store for each project identity, objective, lifecycle, evidence record, artifact revision, and decision state. APOS may maintain task-local projections and propose changes; duplicate authoritative operating ledgers are not the default. Revision conflicts are returned to the owner, never resolved by last-writer-wins without an authorized policy.

## Interoperability boundary

Preserve review, readiness, governance, and execution as separate records. Do not translate template BLOCKED into MDGR block without evaluating the source conditions. Do not collapse hold and escalate. Keep the full canonical verdict contract by reference rather than maintain a competing schema.

The APOS research's Senate/quorum binding is not adopted here: MDGR failure discovery is not voting. AuthZEN adapters, cryptographic identities, state machines, event listeners, and enforcement are outside this delta.

## Targeted validation

Five governance-specific synthetic fixtures cover non-adoption, evidence-plus-authority gaps, PASS without execution authorization, changed artifact approval, and conditional permit. They remain not_executed until actual host outputs and complete evaluation records exist. Structural validation and utility tests do not test their behavior.
