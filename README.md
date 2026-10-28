# Agent Plugin Template

**Copyright © 2026 Rachmat Efendi.**

A reusable **skills-only plugin starter** with a development guide, shared governance, scoped acceptance gates, output contracts, and evaluation fixtures.

Use this repository to build a new domain plugin: a software house, consulting desk, research team, or another task-based workflow. Start from concrete jobs and deliverables rather than a roster of AI personas.

**Template version:** `1.0.0`. **Validation:** see [the validation report](VALIDATION.md); all 11 behavioral scenarios await execution.

## Repository specific development method

This project combines a scoped work contract, evidence-linked analysis, a shared output contract, bounded review, and recorded release evidence. Its authored contribution is the concrete wording, selection, arrangement, fixtures, and software implementation provided in this repository.

| Project-specific implementation | Source |
| --- | --- |
| Objective-bound disposition: assess the requested deliverable without silently substituting a different task | [Output contract](plugin/references/output-contract.md) |
| Separate task disposition from behavioral test outcome, including a correct BLOCKED answer | [Evaluation record](evals/record-template.md) and [cases](evals/cases.json) |
| Require non-empty actual output, structured grading, and matching input/output checksums before accepting an executed case status | [Structural validator](scripts/validate.py) |
| Preserve behavioral instructions during identity customization and package only installable source reproducibly | [Customization](scripts/customize.py), [packaging](scripts/package.py), and [tests](tests/test_developer_tools.py) |
| Preserve accepted artifacts during review and tie changes to an explicit delta and targeted validation | [Review skill](plugin/skills/review-deliverable/SKILL.md) and [development process](docs/development.md) |

See [the repository method](docs/repository-method.md) for its operational sequence and [source provenance](docs/source-provenance.md) for the distinction between project-authored content and public conventions.

See [the final release notes](docs/release-1.0.0.md) and [validation report](VALIDATION.md).

## What is included

- Three usable starter skills: `route-task`, `analyze-evidence`, and `review-deliverable`.
- Shared governance, an output contract, and failure conditions for material work.
- Templates for the plugin brief, capability map, deliverable, and project state.
- Eleven synthetic behavioral cases, kept separate from execution evidence.
- Dependency-free structural validation, deterministic packaging, and tests for these developer utilities.
- An optional Agents SDK integration guide. No agent service, MCP server, API key, event listener, durable state, or runtime enforcement is installed by this template.

The package contains project-authored starter instructions, templates, fixtures, and utilities. Consulting books and client reports are not included.

## Quick start

Requirements: Python 3.10 or newer and Git. The developer scripts use the standard library; no OpenAI API key is needed for structural checks or packaging.

1. Copy or clone the repository into your own workspace.
2. Fill in [the plugin brief](plugin/templates/plugin-brief.md).
3. Rename the plugin directory identity with the customization command below.
4. Adapt the starter skills and [capability map](plugin/templates/capability-map.md) to your actual tasks.
5. Validate, test the utilities, and package the plugin.

```bash
python scripts/customize.py --name my-domain-plugin --display-name "My Domain Plugin" --author "Your Name"
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/package.py
```

The package is written under `dist/` and contains only one plugin directory. Repository documentation, tests, and development evidence stay outside the installable package.

The customization command updates the manifest identity and presentation. It does **not** invent domain expertise or rewrite your skills, acceptance criteria, or capability map. Replace the generic description and default prompt in `plugin/plugin.json` before your own release.

## Repository layout

| Path | Purpose |
| --- | --- |
| `plugin/plugin.json` | Portable Agent Plugins 1.0 manifest and OpenAI presentation metadata |
| `plugin/skills/` | Task-specific SKILL.md files and optional host UI metadata |
| `plugin/references/` | Shared governance, output contract, acceptance gates, and source discipline |
| `plugin/templates/` | Blank reusable work structures, including non-persisted state |
| `docs/` | Development process, orchestration choices, SDK extension path, and release checklist |
| `evals/cases.json` | Synthetic prompts and criteria; all start as not executed |
| `evals/results/` | Local actual outputs and evaluation evidence; ignored by Git by default |
| `scripts/` | Structural validation, manifest customization, and packaging |
| `tests/` | Deterministic tests of developer utilities, not model behavior |

## Design a domain plugin

### 1 Define the work contract

Specify the user, objective, inputs, deliverable, operating context, decision owner, tools, exclusions, authorization, and acceptance threshold. Ask only about gaps that materially affect those fields. Do not infer execution permission from a discussion request.

### 2 Map jobs to capabilities

Use short verb-led names, such as `model-financials`, `review-contract`, or `design-architecture`. Split skills when their triggers, methods, outputs, or acceptance criteria differ. Divisions organize capabilities; they are not a mandate to activate every role.

Retain a routing owner and accountable synthesis owner when tasks cross multiple capabilities. A narrow task may need only one skill.

### 3 Keep instructions layered

Metadata helps the host select a skill. SKILL.md contains the operational workflow. Load references and templates selectively. Keep shared rules in one source and link to them from relevant skills.

Do not duplicate governance across every skill. Add domain methods when a real use case or failed behavior test reveals a method gap.

### 4 Write measurable acceptance criteria

State when a task passes, passes with non-blocking notes, or is blocked. Test the failure modes that matter: fabricated numbers, missing evidence, unauthorized changes, invented professional sources, unsupported charts, false persistence, and authority creep.

An incomplete material valuation should remain blocked. Do not substitute an evidence-gap memo and call the requested valuation complete. Conversely, a scoped evidence-gap diagnosis can pass without proving the underlying claim.

### 5 Execute behavior tests before making behavior claims

Use [the cases](evals/cases.json) as a starting matrix. Give the host the skill and raw task-local input; keep the grading criteria outside the tested agent's context. Save the actual answer before assigning a grade.

Record input, artifact version, instruction snapshot or commit, host/model, actual output, checks, task disposition, behavioral outcome, evaluator, and limitations using [the evaluation instructions](evals/record-template.md) and [JSON record template](evals/record-template.json). Every case remains `not_executed` until an actual run is recorded.

**Task disposition and behavioral outcome are different fields.** A correctly blocked unsupported claim can pass its behavioral test. A polished answer with fabricated evidence fails.

Independent evidence requires an independent source or procedure. Multiple outputs from one model are not external professional validation.

### 6 Test the installed host separately

Use [the host acceptance checklist](docs/host-acceptance.md) to verify discovery, routing, tools, reference access, permissions, and any file deliverables in the target host. A local instruction test does not demonstrate installed plugin auto-discovery. Test DOCX/PPTX/XLSX/PDF generation and rendering only if those capabilities are part of your scope.

### 7 Release a bounded baseline

Use [the release checklist](docs/release-checklist.md). Preserve identity, audience, and unspecified content on updates. Promote an accepted RC without new behavior only when the authorized delta is release metadata; inherited tests remain inherited evidence.

Follow `Baseline → Delta → Impact → Targeted validation`. Optional improvements alone do not reopen accepted work.

## Governance and authority

The [shared governance](plugin/references/governance.md) is an instruction profile, not a host-enforced security boundary. The applicable user/project governance and authorized human decision owner remain authoritative. If AFGS/MDGR applies, retain its decision-governance precedence without copying or claiming adoption of its kernel.

Every consolidated analytical output closes with [the output contract](plugin/references/output-contract.md): objective and authorization, claim classes, performed/unperformed checks, decision-changing limitations, authority status, and disposition.

Discussion, recommendation, decision, approval, authorization, execution, and validation are distinct. A completed artifact is not client acceptance, implementation, statutory filing, professional sign-off, or realized business benefit.

## Orchestration choices

| Need | Pattern | Add only when |
| --- | --- | --- |
| Capability routing | Hub-and-spoke | One request needs a selected workflow |
| Work allocation | Supervisor–Worker | Independent subtasks materially help |
| Dependency management | DAG | Some tasks depend on other outputs |
| Shared state | Governed blackboard | Provenance and revision ownership are explicit |
| Iterative quality | Producer–Critic | A bounded review loop improves the artifact |
| Material synthesis | Committee + Judge | Specialists provide findings to an authorized owner |
| Long-running triggers | Event-driven | A real runtime implements and audits events |

These are design options. The starter implements instruction-level routing and review only. See [orchestration guidance](docs/orchestration.md).

## Optional governance integration

Use the [integration guide](docs/governance-integration.md) when AFGS, MDGR, or a project operating layer is relevant. Keep cited prior work separate from scoped policy adoption. Fill the [governance profile](plugin/templates/governance-profile.md) only as needed; it defaults to reference-only.

Review acceptance, decision readiness, governance outcome, and execution authorization remain distinct. Preserve MDGR's canonical contract when explicitly adopted. Assign one authoritative state owner when APOS and AI Founder OS coexist. Source pins and maturity limits are recorded in [provenance](docs/source-provenance.md).

For coordination needs, use the [orchestration profile](plugin/templates/orchestration-profile.md). The single-owner default remains; no agent roster or runtime is added.

## Optional Agents SDK extension

Read [the integration guide](docs/agents-sdk.md) before adding a runtime. Start with one real agent path; introduce tools, handoffs, state, or sandboxing only when the work contract requires them. Keep the runtime in a separate project or directory and outside the plugin package.

A runtime must explicitly load or connect these instructions using a supported host mechanism. Markdown files do not automatically become Agent definitions, handoffs, permissions, persistent sessions, or tool policies.

## Packaging and installation

`python scripts/package.py` first runs structural validation, rejects symlinks, and packages the `plugin/` source as `<manifest-name>/...` in a tar.gz archive. Before completing packaging, the command extracts the archive and verifies contained Markdown links plus manifest and copyright integrity. It does not install or publish the plugin.

The root manifest uses the portable plugin package format. If a particular client requires a compatibility overlay such as `.codex-plugin/plugin.json`, add it only for that client and synchronize identity, version, and presentation. Validate that overlay in the client before claiming support.

Use the target host's private import or plugin-creation workflow with the resulting archive. Installation, directory submission, and public publication are separate actions. No automatic public publishing is configured here.

## GitHub reuse

See [upload instructions](docs/upload-to-github.md) for creating a new repository and pushing the source.

The repository can be marked as a GitHub template through its settings after creation. Clone it normally if that setting is not enabled. Choose the owner and visibility explicitly for each derived repository; private is the working default.

Commit only authorized project sources. Never commit client data, secrets, restricted literature, or API keys. Evaluation results are ignored by default; commit only reviewed, sanitized evidence if your policy allows it.

## Validation limits

`scripts/validate.py` checks this starter's conventions: manifest shape, naming, frontmatter, UI prompt references, internal link existence, state default, package-reference containment, and structured execution records with input/output checksum matching. It is **not** a full upstream JSON Schema validator or a runtime security scanner.

`tests/` checks actual developer scripts, including rejected invalid metadata and packaging behavior. Neither these tests nor the structural checker execute an LLM or the eleven behavioral fixtures.

## Copyright and license

**Copyright © 2026 Rachmat Efendi.** Licensed under the [MIT License](LICENSE).

The MIT License covers the original repository text, selection and arrangement of materials, and software implementation. Public specifications, general methods, and third-party materials retain their respective provenance and terms. See [the copyright notice](COPYRIGHT.md).

## Primary references

- [OpenAI agent guide](https://developers.openai.com/api/docs/guides/agents)
- [OpenAI agent evaluations](https://developers.openai.com/api/docs/guides/agent-evals)
- [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python)
- [OpenAI Agents SDK TypeScript](https://github.com/openai/openai-agents-js)
- [OpenAI plugins](https://github.com/openai/plugins)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Anthropic skills](https://github.com/anthropics/skills)

Check current primary documentation at implementation time.
