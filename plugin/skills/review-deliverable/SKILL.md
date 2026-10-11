---
name: review-deliverable
description: "Review a specific artifact against scoped criteria without editing its baseline. Use for review-only, locked artifact validation, consistency checks, and release review."
---

# Review Deliverable

## Resources and boundary

Read [shared governance](../../references/governance.md) before substantive work. Reuse the same version if already loaded. Apply the relevant [acceptance gates](../../references/acceptance-gates.md), [source discipline](../../references/source-discipline.md), and [output contract](../../references/output-contract.md).

Use the [deliverable template](../../templates/deliverable.md) only when useful. Follow actual user/project authority and available host capabilities.

## Inputs

Requested objective, authorization, artifact/version if supplied, evidence, scope, and acceptance criteria. Ask only for a material missing input; do not invent unavailable data or tool access.

## Workflow

1. Bind the review to the artifact version and requested criteria. Keep a locked or accepted baseline intact.
2. Inspect only material scope, evidence, calculations, consistency, and authority boundaries relevant to those criteria.
3. Report findings by reference with effect and requested remedy. Separate blockers from optional improvements.
4. Use BLOCKED for material failed criteria; PASS WITH NON-BLOCKING NOTES for optional issues; PASS when scoped criteria are satisfied.
5. Stop after the required checks. Do not revise the artifact or reopen unrelated conclusions. Disclose checks not performed.

## Output and acceptance

Version-bound review findings and disposition. BLOCKED if the requested review cannot be completed against material criteria. No baseline edit is authorized by this skill. Report actual checks, decision-changing limitations, and authority status using the shared output contract. Stop when scope and required checks are complete.
