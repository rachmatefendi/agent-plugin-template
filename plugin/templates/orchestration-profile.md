# Optional orchestration profile

Fill only the choices needed for the task. Default to one owner and the minimum relevant skill set. This profile does not launch agents or install a runtime.

- topology: single-owner
- execution_pattern: single-worker
- workflow_dependencies: []
- state_refs_and_expected_revisions: []
- authoritative_state_owner:
- synthesis_owner:
- decision_owner:
- review_acceptance_criteria: []
- max_review_iterations:
- stop_and_escalation_conditions:
- activation: user-request
- event_runtime_evidence_ref: not-established

Workers return findings and proposed deltas. A state writer checks scope and expected revision before accepting updates. Exhausting review time/iterations with a material blocker does not yield PASS. Event-triggered activation may be claimed only when an actual runtime and observed event path exist. Topology never grants authority.
