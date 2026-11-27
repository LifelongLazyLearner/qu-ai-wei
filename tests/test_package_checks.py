"""Counterexamples for repository validators that previously skipped malformed input."""
import tempfile
import unittest
from pathlib import Path

from skill_checks.common import EvalError
from skill_checks.package import REQUIRED_REFERENCES, check_references, check_triggers


class PackageChecks(unittest.TestCase):
    def test_invalid_trigger_expectation_does_not_get_skipped(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / 'trigger-manifest.txt'
            manifest.write_text(
                '[01]\nquery=q\nexpect=TRIGGER\nanchor=present\n'
                '[02]\nquery=q\nexpect=TYPO\nanchor=present\n',
                encoding='utf-8',
            )
            with self.assertRaisesRegex(EvalError, '02: expected TRIGGER or EXCLUDE'):
                check_triggers('present', manifest)

    def test_route_must_be_a_local_link_to_the_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'references').mkdir()
            (root / 'tests/blind-review').mkdir(parents=True)
            for document in ('README.md', 'tests/README.md', 'tests/blind-review/README.md'):
                (root / document).touch()
            names = sorted(REQUIRED_REFERENCES)
            for name in names:
                (root / 'references' / name).touch()
            routes = '\n'.join(f'[rule](./references/{name}#section)' for name in names)
            (root / 'SKILL.md').write_text(routes, encoding='utf-8')
            check_references(root, routes)

            omitted = routes.replace(f'[rule](./references/{names[0]}#section)', f'`references/{names[0]}`')
            with self.assertRaisesRegex(EvalError, 'SKILL.md does not route to'):
                check_references(root, omitted)
            (root / 'README.md').write_text('[missing](./references/missing.md)', encoding='utf-8')
            with self.assertRaisesRegex(EvalError, 'README.md: broken local link'):
                check_references(root, routes)
