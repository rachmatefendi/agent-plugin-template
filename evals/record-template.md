# Behavioral evaluation records

Copy record-template.json into evals/results/ after saving the actual output. Populate every identity field with real run information. Use an ISO timestamp with a timezone. Record the exact source commit or instruction snapshot in instruction_revision.

For the corresponding case in cases.json, set actual_output and evaluation_record to contained repository-relative file paths. Set execution_status to executed only after actual execution and assessment.

## Required grading fields

- task_disposition: BLOCKED / PASS WITH NON-BLOCKING NOTES / PASS.
- behavior_outcome: PASS / FAIL, independently of task disposition.
- checks_performed: at least one actual check.
- checks_not_performed and limitations: arrays; empty only when appropriate within scope.
- criterion_assessments: one object per criterion, in the original order, with criterion_index starting at 1, outcome PASS/FAIL, and a non-empty rationale. Any failed criterion makes behavior_outcome FAIL.

## Bind records to actual bytes

Calculate input_sha256 using scripts/validate.py input_digest(case), which canonicalizes skill, prompt, and context as sorted JSON with ensure_ascii=False. Calculate output_sha256 as the SHA256 of saved raw output bytes. Changing those inputs or output requires reassessment and updated records.

From the repository root, compute both values for a completed case after setting its actual_output path:

```python
import hashlib, json, sys
from pathlib import Path
sys.path.insert(0, "scripts")
from validate import input_digest
cases = json.loads(Path("evals/cases.json").read_text())["cases"]
case = next(c for c in cases if c["id"] == "small-routing")
print("input_sha256:", input_digest(case))
print("output_sha256:", hashlib.sha256(Path(case["actual_output"]).read_bytes()).hexdigest())
```

Keep grading criteria and records outside the tested agent's input. The validator checks structural completeness and checksum matching; it cannot establish that an evaluator's narrative is truthful or that a model run actually occurred.
