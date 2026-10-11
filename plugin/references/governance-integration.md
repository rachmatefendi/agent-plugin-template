# Optional governance integration

Load this reference only when external governance is relevant. Record applicability and adoption in the [governance profile](../templates/governance-profile.md). Citation alone never activates governance or creates approval authority.

## Separate status domains

| Field | Meaning | Allowed representation |
| --- | --- | --- |
| review_disposition | Acceptance against the requested artifact criteria | BLOCKED / PASS WITH NON-BLOCKING NOTES / PASS |
| decision_readiness | Completeness for the specified authority gate | ready / not-ready / unresolved |
| governance_outcome | Result under the adopted governance contract | Exact source vocabulary, with provenance; absent if not evaluated |
| execution_authorization | Separate current permission for a specific action | not-established / externally-established, with evidence reference |

Do not map review PASS to governance permit or execution permission. A BLOCKED analytical task does not by itself establish a governance `block`; it may reflect missing evidence. Do not fabricate evaluated statuses to fill empty fields. Model-generated objects are candidate/advisory outputs unless authenticated external records establish otherwise.

## MDGR compatibility

For an explicitly adopted MDGR v1.0 profile, preserve its canonical `verdict` object and rules in the pinned [specification sections 12–14](https://github.com/rachmatefendi/material-decision-governance-runtime/blob/0bc1377270d3ca962df0787cdbe1b59d83364691/SPECIFICATION.md). Put specialist recommendations and review status outside `verdict`.

Canonical outcome tokens are `permit`, `permit_with_conditions`, `hold`, `escalate`, `block`. Resolution priority is block, hold, escalate, permit_with_conditions, permit under the source's qualifying conditions. A critical evidence gap yields hold while any authority gap remains explicit; once otherwise ready, unresolved authority yields escalate unless block takes precedence. Conditional permit requires authority sufficiency and explicit binding conditions. Failure discovery supplies findings, not decision votes.

Neither permit nor a model-produced `execution.authorized` field grants execution permission. Only record established authorization when separate current evidence supports actor, action, scope, artifact revision/digest, target, parameters, conditions, validity, and applicable revalidation checks. A changed material artifact or scope requires renewed evaluation before reuse.

## AFGS and APOS mapping

AFGS supplies the governance architecture; MDGR addresses material-decision semantics; APOS research proposes a project operating layer; skills provide reusable task methods. Their identities and roles are distinct. Document state ownership when combining them.

The AFGS public repository contains a paper and non-normative companions, not a verified canonical DOCX. It describes conjunctive execution eligibility: any mandatory false or unresolved term prevents that consequential execution attempt. It does not establish a live permission gateway. See the pinned [execution companion](https://github.com/rachmatefendi/afgs-agentic-ai-governance/blob/351069cd50e078b3e8e0be0fe905d26bc6ff01fc/architecture/execution-semantics.md).

This starter includes no AFGS/MDGR engine, authority registry, execution token issuer, cryptographic state service, or APOS runtime. Its instructions and templates must not be described as those controls.
