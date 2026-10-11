# Orchestration and handoffs

Distinguish topology, execution pattern, workflow dependency, and decision authority. Use hub-and-spoke routing plus supervisor–worker execution when useful; add DAG dependencies and governed shared state only when warranted.

Producer–critic loops need finite acceptance criteria and stop rules. Committee findings are inputs to an authorized synthesis/decision owner, not votes from AI personas. Event-driven behavior needs a real event runtime. Tree, federated hubs, task auctions, or swarm designs are optional architectural choices, not starter capabilities.

## Handoff contract

Include objective, scope, authorization class, input references, artifact revision, owner, output, dependencies, acceptance criteria, stop rule, and escalation condition. Workers propose deltas; actual permissions and revision controls belong to the host/backend.

## State boundary

The project-state template starts not-persisted. Markdown does not implement locks, durable memory, transactions, audit logs, or automated revalidation. Implement and test those properties before claiming them.

## Select patterns by function

Use the [optional profile](../plugin/templates/orchestration-profile.md) only when coordination materially helps.

| Function | Options | Selection boundary |
| --- | --- | --- |
| Relationship topology | Hub-and-spoke, hierarchical/tree, federated/multi-hub | Add intermediate owners only for actual coordination needs |
| Work allocation | Supervisor–worker, contract-net/task auction | Auction requires a real capability registry and routing policy |
| Dependencies | Pipeline/DAG | Parallelize independent work; represent review iteration separately from an acyclic dependency graph |
| Shared knowledge | Blackboard | Explicit writer, expected revision, provenance, and conflict handling |
| Quality and synthesis | Producer–critic, committee + judge | Bounded review; findings do not confer approval authority |
| Activation | User request, event-driven/pub-sub | Events require implemented and tested infrastructure |
| Decentralized coordination | Swarm | Optional; requires demonstrated control, ownership, and auditability before consequential use |

An AI research engagement may combine hub-and-spoke routing, supervisor–worker allocation, a DAG for evidence/evaluation dependencies, and a blackboard for referenced state. The synthesis owner integrates findings; the designated human/organizational owner retains decision authority. A small task should retain the single-owner default.
