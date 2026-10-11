# Source provenance

## Project authored material

The README, operational instructions, shared contracts, templates, synthetic evaluation cases, developer utilities, tests, and development documents were prepared for this project through Rachmat Efendi's design direction and revisions with AI assistance. The human design decisions include task proportionality, evidence classifications, authority separation, review convergence, bounded changes, and release-evidence requirements. Git commits record source revisions; they are not a registration certificate.

The project-specific contribution is its wording, selection, arrangement, fixtures, and implementation. This record does not classify general methods as exclusive inventions.

## Public conventions and external references

| Convention | Reference and use |
| --- | --- |
| Skill folders and YAML frontmatter | OpenAI and Anthropic skills conventions; used for interoperability |
| Plugin manifest and presentation metadata | Agent Plugins schema and host packaging guidance; used for package identity |
| Skill UI metadata | OpenAI skill tooling conventions; generated values match the starter skills |
| Progressive loading and selective references | Existing skill design practice; used to control context size |
| Supervisor–worker, DAG, blackboard, and critic loops | General orchestration patterns; documented as architectural options |
| Unit tests, Git history, checksums, and reproducible archives | General software-development techniques; used by project utilities |

## Material outside this source package

The helper tools used to initialize and validate the skills are outside the repository. Their generated SKILL.md bodies were replaced by project-specific instructions. The generated UI metadata follows the public host format. No upstream helper implementation, book summary, consulting report, adopted governance kernel, or client data is bundled.

## Primary reference links

- https://github.com/openai/plugins
- https://github.com/anthropics/skills
- https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- https://developers.openai.com/api/docs/guides/agents

Record source and license details before adding any third-party content in future revisions.

## Governance and project research lineage

References inspected on 2026-10-11. Public repository availability establishes a public source, not global novelty or implementation conformance. Commit pins identify retrieved revisions; they do not validate the claims in those files.

| Source | Pinned identity | Use and document class |
| --- | --- | --- |
| MDGR v1.0 | [Commit 0bc1377270d3ca962df0787cdbe1b59d83364691](https://github.com/rachmatefendi/material-decision-governance-runtime/tree/0bc1377270d3ca962df0787cdbe1b59d83364691), SPECIFICATION.md sections 12–14 | Public specification; canonical outcome and verdict semantics; implementation not claimed |
| AFGS v1.0 | [Commit 351069cd50e078b3e8e0be0fe905d26bc6ff01fc](https://github.com/rachmatefendi/afgs-agentic-ai-governance/tree/351069cd50e078b3e8e0be0fe905d26bc6ff01fc), README.md, provenance/README.md, architecture/execution-semantics.md | Publication and non-normative companions; canonical DOCX absent and declared hash not verified |
| APOS Architecture Deep Research | User-supplied DOCX snapshot; SHA-256: 2586b891d2787a96f1f2cb98a98fed540cbff85e1caa262da53a74538e46a5f7 | Internal architecture research; no verified public release or adopted normative status |

The original PDF, DOCX, source excerpts, and verdict schema are not bundled. Repository-authored mapping notes remain separate. MDGR declares Apache-2.0 for its repository except explicit exclusions; AFGS's paper retains CC BY-ND 4.0, and its companions declare no separate license grant. These source notices are not a license for this entire template.

See [the integration design](governance-integration.md). APOS report ratings and suggested experiments are not benchmark outcomes. This release adopts no Senate voting requirement and makes no mathematical-minimal-context or runtime-isolation claim.
