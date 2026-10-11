# Development process

1. Fill the brief and resolve material ambiguity.
2. Map jobs to task-based capabilities and one synthesis owner.
3. Separate shared rules, task instructions, methods, templates, and runtime.
4. Implement only the authorized scope; keep references selectively loaded.
5. Run structural checks and utility tests. Fix observed failures.
6. Execute raw behavioral cases on the real host path and save actual outputs.
7. Test installed discovery, tools, and file deliverables separately when in scope.
8. Review with BLOCKED / PASS WITH NON-BLOCKING NOTES / PASS.
9. Freeze a bounded baseline and promote only after the agreed release gate.
10. Maintain through Baseline → Delta → Impact → Targeted validation.

## Lessons from prior development

The Virtual Consulting Firm development emphasized explicit output contracts, shared fail gates for material skills, external governance precedence, non-runtime state templates, and actual scenario evidence. Use these principles without copying its scope or books. This starter has its own unexecuted behavior cases and inherits no behavior PASS from that plugin.

## Stop rule

Stop when the objective and required checks are met, no material blocker remains, and no decision-changing unknown remains within the requested scope. Optional improvements do not justify reopening an accepted baseline.
