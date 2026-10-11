import json
import hashlib
import shutil
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate import validate, input_digest
from customize import customize
from package import package

class DeveloperToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', 'dist', '__pycache__'))

    def tearDown(self):
        self.temp.cleanup()

    def test_baseline_structure(self):
        self.assertEqual([], validate(self.root))

    def test_identity_customization_preserves_skills(self):
        path = self.root / 'plugin/skills/analyze-evidence/SKILL.md'
        baseline = path.read_bytes()
        customize(self.root, 'new-plugin', 'New Plugin', 'New Author')
        self.assertEqual(baseline, path.read_bytes())
        self.assertEqual([], validate(self.root))
        manifest = json.loads((self.root / 'plugin/plugin.json').read_text())
        self.assertEqual('new-plugin', manifest['name'])

    def test_bad_identity_rejected_before_mutation(self):
        path = self.root / 'plugin/plugin.json'
        baseline = path.read_bytes()
        with self.assertRaises(ValueError):
            customize(self.root, '../escape', 'Bad', 'Author')
        self.assertEqual(baseline, path.read_bytes())

    def test_missing_evidence_cannot_be_marked_executed(self):
        path = self.root / 'evals/cases.json'
        data = json.loads(path.read_text())
        data['cases'][0]['execution_status'] = 'executed'
        path.write_text(json.dumps(data))
        self.assertTrue(any('executed requires' in e for e in validate(self.root)))

    def test_broken_skill_link_fails(self):
        (self.root / 'plugin/references/governance.md').unlink()
        self.assertTrue(any('broken/escaping link' in e for e in validate(self.root)))

    def test_archive_is_reproducible_and_contains_only_plugin(self):
        output = package(self.root)
        first = output.read_bytes()
        self.assertEqual(first, package(self.root).read_bytes())
        with tarfile.open(output) as archive:
            names = archive.getnames()
        self.assertTrue(all(n.startswith('agent-plugin-template/') for n in names))
        self.assertIn('agent-plugin-template/plugin.json', names)
        self.assertIn('agent-plugin-template/COPYRIGHT.md', names)
        self.assertFalse(any(n.endswith('README.md') or '/evals/' in n for n in names))

    def test_symlink_rejected(self):
        (self.root / 'plugin/leak.md').symlink_to(self.root / 'README.md')
        with self.assertRaises(ValueError):
            package(self.root)

    def executed_fixture(self):
        path = self.root / 'evals/cases.json'
        data = json.loads(path.read_text())
        case = data['cases'][0]
        case.update(execution_status='executed', actual_output='evals/results/output.md', evaluation_record='evals/results/record.json')
        # Synthetic records test utility validation only; they are not model runs.
        output = self.root / case['actual_output']
        output.write_text('Synthetic utility-test output.\n')
        record = dict(case_id=case['id'], executed_at='2026-10-11T01:00:00+07:00', instruction_revision='utility-test-fixture',
                      host='unit-test', model='not-an-LLM-run', evaluator='unit-test', state_isolation='temporary-copy',
                      input_sha256=input_digest(case), output_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),
                      task_disposition='PASS', behavior_outcome='PASS', checks_performed=['fixture validation'],
                      checks_not_performed=['model behavior'], limitations=['synthetic utility test'],
                      criterion_assessments=[dict(criterion_index=i+1, outcome='PASS', rationale='Synthetic test grade') for i in range(len(case['criteria']))])
        record_path = self.root / case['evaluation_record']
        record_path.write_text(json.dumps(record))
        path.write_text(json.dumps(data))
        return case, record, record_path

    def test_complete_record_is_structurally_accepted(self):
        self.executed_fixture()
        self.assertEqual([], validate(self.root))

    def test_correct_blocked_task_can_have_passing_behavior(self):
        _, record, path = self.executed_fixture()
        record['task_disposition'] = 'BLOCKED'
        path.write_text(json.dumps(record))
        self.assertEqual([], validate(self.root))

    def test_empty_execution_files_fail(self):
        case, _, record_path = self.executed_fixture()
        (self.root / case['actual_output']).write_text('  \n')
        record_path.write_text('')
        self.assertTrue(any('non-empty contained' in e for e in validate(self.root)))

    def test_changed_output_fails_checksum(self):
        case, _, _ = self.executed_fixture()
        (self.root / case['actual_output']).write_text('Changed output')
        self.assertTrue(any('output checksum mismatch' in e for e in validate(self.root)))

    def test_incomplete_grading_and_missing_identity_fail(self):
        _, record, path = self.executed_fixture()
        record['criterion_assessments'] = []
        record['instruction_revision'] = ''
        path.write_text(json.dumps(record))
        errors = validate(self.root)
        self.assertTrue(any('incomplete criterion' in e for e in errors))
        self.assertTrue(any('instruction_revision' in e for e in errors))

    def test_case_and_input_mismatch_fail(self):
        _, record, path = self.executed_fixture()
        record['case_id'] = 'different-case'
        record['input_sha256'] = '0' * 64
        path.write_text(json.dumps(record))
        errors = validate(self.root)
        self.assertTrue(any('record case mismatch' in e for e in errors))
        self.assertTrue(any('input checksum mismatch' in e for e in errors))

    def test_failed_criterion_cannot_report_behavior_pass(self):
        _, record, path = self.executed_fixture()
        record['criterion_assessments'][0]['outcome'] = 'FAIL'
        path.write_text(json.dumps(record))
        self.assertTrue(any('contradicts' in e for e in validate(self.root)))

    def test_link_to_repository_docs_is_rejected_from_plugin(self):
        (self.root / 'plugin/references/outside.md').write_text('[Docs](../../docs/development.md)')
        self.assertTrue(any('reference outside package' in e for e in validate(self.root)))
        with self.assertRaises(ValueError):
            package(self.root)

    def test_missing_copyright_blocks_packaging(self):
        (self.root / 'plugin/COPYRIGHT.md').unlink()
        with self.assertRaises(ValueError):
            package(self.root)

if __name__ == '__main__':
    unittest.main()
