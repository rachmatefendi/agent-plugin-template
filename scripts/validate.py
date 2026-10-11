"""Check starter conventions only; no LLM or upstream schema validation."""
import json
import hashlib
from datetime import datetime
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
VERSION = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?")

def validate_plugin_links(plugin):
    plugin = Path(plugin).resolve()
    errors = []
    for file in sorted(plugin.rglob('*.md')):
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', file.read_text()):
            url = urlsplit(target)
            if url.scheme or target.startswith('#'):
                continue
            resolved = (file.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(plugin) or not resolved.exists():
                errors.append(f'{file.relative_to(plugin)}: reference outside package or missing: {target}')
    return errors

def input_digest(case):
    payload = {k: case.get(k, '') for k in ('skill', 'prompt', 'context')}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

def validate_execution(root, case):
    errors = []
    paths = {}
    for key in ('actual_output', 'evaluation_record'):
        value = case.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{case['id']}: executed requires {key}")
            continue
        path = (root / value).resolve()
        if not path.is_relative_to(root) or not path.is_file() or not path.read_bytes().strip():
            errors.append(f"{case['id']}: executed requires non-empty contained {key}")
        else:
            paths[key] = path
    if len(paths) != 2:
        return errors
    try:
        record = json.loads(paths['evaluation_record'].read_text())
        for key in ('case_id', 'executed_at', 'instruction_revision', 'host', 'model', 'evaluator', 'state_isolation'):
            if not isinstance(record.get(key), str) or not record[key].strip():
                errors.append(f"{case['id']}: missing record field {key}")
        if record.get('case_id') != case['id']:
            errors.append(f"{case['id']}: record case mismatch")
        when = datetime.fromisoformat(record.get('executed_at', '').replace('Z', '+00:00'))
        if when.tzinfo is None:
            errors.append(f"{case['id']}: executed_at needs a timezone")
        if record.get('input_sha256') != input_digest(case):
            errors.append(f"{case['id']}: input checksum mismatch")
        if record.get('output_sha256') != hashlib.sha256(paths['actual_output'].read_bytes()).hexdigest():
            errors.append(f"{case['id']}: output checksum mismatch")
        if record.get('task_disposition') not in ('BLOCKED', 'PASS WITH NON-BLOCKING NOTES', 'PASS'):
            errors.append(f"{case['id']}: invalid task disposition")
        if record.get('behavior_outcome') not in ('PASS', 'FAIL'):
            errors.append(f"{case['id']}: invalid behavior outcome")
        for key in ('checks_performed', 'checks_not_performed', 'limitations'):
            if not isinstance(record.get(key), list) or not all(isinstance(v, str) and v.strip() for v in record.get(key, [])):
                errors.append(f"{case['id']}: {key} must be an array of non-empty strings")
        if not record.get('checks_performed'):
            errors.append(f"{case['id']}: at least one performed check required")
        assessments = record.get('criterion_assessments', [])
        if not isinstance(assessments, list) or len(assessments) != len(case['criteria']):
            errors.append(f"{case['id']}: incomplete criterion assessments")
        else:
            for i, assessment in enumerate(assessments):
                if (not isinstance(assessment, dict) or assessment.get('criterion_index') != i + 1
                    or assessment.get('outcome') not in ('PASS', 'FAIL')
                    or not isinstance(assessment.get('rationale'), str) or not assessment['rationale'].strip()):
                    errors.append(f"{case['id']}: invalid criterion assessment {i + 1}")
            outcomes = [a.get('outcome') for a in assessments if isinstance(a, dict)]
            expected = 'FAIL' if 'FAIL' in outcomes else 'PASS'
            if record.get('behavior_outcome') != expected:
                errors.append(f"{case['id']}: behavior outcome contradicts criterion grades")
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        errors.append(f"{case['id']}: invalid evaluation record: {exc}")
    return errors

def validate(root=ROOT):
    root = Path(root).resolve()
    plugin = root / 'plugin'
    errors = []
    errors.extend(validate_plugin_links(plugin))
    if not (plugin / 'COPYRIGHT.md').is_file():
        errors.append('Plugin copyright notice required')
    try:
        manifest = json.loads((plugin / 'plugin.json').read_text())
        name = manifest['name']
        if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
            errors.append('Invalid manifest name')
        if not VERSION.fullmatch(manifest['version']):
            errors.append('Invalid semantic version')
        if not manifest.get('description') or not manifest['author'].get('name'):
            errors.append('Description and author are required')
        interface = manifest['extensions']['com.openai']['interface']
        if not 1 <= len(interface['shortDescription']) <= 30:
            errors.append('Plugin shortDescription must contain 1–30 characters')
        if any(k in manifest for k in ('skills', 'mcpServers', 'apps', 'interface')):
            errors.append('Unsupported top-level portable manifest keys')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append('Invalid manifest: ' + str(exc))
    skills = sorted((plugin / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('No skills found')
    for skill in skills:
        text = skill.read_text()
        match = re.match(r'\A---\nname: ([^\n]+)\ndescription: ("[^\n]+")\n---\n', text)
        if not match:
            errors.append(f'{skill.name}: expected name and quoted description frontmatter')
            continue
        name = match[1]
        if name != skill.parent.name or not NAME.fullmatch(name) or len(name) > 64:
            errors.append(f'{skill.parent.name}: skill identity mismatch')
        try:
            if not json.loads(match[2]).strip():
                errors.append(f'{name}: empty description')
            ui = (skill.parent / 'agents/openai.yaml').read_text()
            if '$' + name not in ui:
                errors.append(f'{name}: UI prompt must mention the skill')
        except (ValueError, OSError) as exc:
            errors.append(f'{name}: metadata error {exc}')
        for required in ('## Inputs', '## Workflow', '## Output and acceptance'):
            if required not in text:
                errors.append(f'{name}: missing {required}')
    for file in sorted(root.rglob('*')):
        if any(x in file.relative_to(root).parts for x in ('.git', 'dist', '__pycache__', 'results')):
            continue
        if file.is_symlink():
            errors.append(f'Symlink rejected: {file.relative_to(root)}')
            continue
        if file.suffix != '.md' or not file.is_file():
            continue
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', file.read_text()):
            url = urlsplit(target)
            if url.scheme or target.startswith('#'):
                continue
            resolved = (file.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f'{file.relative_to(root)}: broken/escaping link {target}')
    try:
        state = (plugin / 'templates/project-state.md').read_text()
        if 'persistence_status: not-persisted' not in state:
            errors.append('State must default to not-persisted')
        cases = json.loads((root / 'evals/cases.json').read_text())['cases']
        ids = [case['id'] for case in cases]
        if len(ids) != len(set(ids)):
            errors.append('Duplicate case ids')
        for case in cases:
            if not case.get('criteria') or not case.get('prompt'):
                errors.append(f"{case['id']}: missing criteria/prompt")
            if case['execution_status'] not in ('not_executed', 'executed'):
                errors.append(f"{case['id']}: invalid execution status")
            if case['execution_status'] == 'executed':
                errors.extend(validate_execution(root, case))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append('Invalid state/cases: ' + str(exc))
    return errors

if __name__ == '__main__':
    problems = validate()
    for problem in problems:
        print('ERROR:', problem)
    print('Structural checks:', 'FAIL' if problems else 'PASS')
    print('Behavior cases are not executed by this checker.')
    sys.exit(bool(problems))
