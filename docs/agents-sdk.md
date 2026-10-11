# Optional Agents SDK integration

This repository is a skills-only source template. It contains no runnable Agents SDK service and does not need an API key. Add an SDK runtime as a separate, explicitly scoped project when the objective requires live tools, sessions, handoffs, or automation.

## Extension workflow

1. Read the current OpenAI agent guide and target SDK documentation.
2. Define the real input/output contract, tools, state, permissions, approval boundaries, and smoke command.
3. Start with a single Agent and Runner path using the installed SDK's documented interfaces. Do not create multiple agents merely to mirror a firm organization chart.
4. Explicitly connect/load the chosen instructions and references; do not assume automatic plugin discovery by the SDK.
5. Add deterministic tools with narrow side effects. Enforce authorization and concurrency in tools/backend rather than prompts alone.
6. Use SandboxAgent only for supported workspace tasks; read the current sandbox guide before implementing its APIs or backend behavior.
7. Obtain API access through the host's credential workflow if needed. Never commit or print secrets.
8. Exercise the actual agent path with isolated/reset state. Save actual outputs/traces and evaluate behavior, tool calls, state changes, and authorization boundaries.
9. Keep runtime dependencies and deployment files outside plugin/. Deploy only when requested and separately verify service readiness.

## Required evidence before claims

Record the installed SDK version, model, tools, host, actual smoke result, failure cases, and unperformed checks. A successful model answer does not prove persistence, permission enforcement, production readiness, professional accuracy, or external validation.

## Primary documentation

- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents/sandboxes
- https://developers.openai.com/api/docs/guides/agent-evals
- https://github.com/openai/openai-agents-python
- https://github.com/openai/openai-agents-js

Verify the SDK interfaces against the installed version before writing executable code.
