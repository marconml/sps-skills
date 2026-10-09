"""De-identified install/update/recovery canaries; no network or live install."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import sync_skill

class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.target = Path(self.tmp.name) / 'skills' / sync_skill.SKILL
    def release(self, text='version one', sha='a'*40):
        def fetch(stage):
            (stage / 'SKILL.md').write_text(text)
            (stage / 'references').mkdir()
            (stage / 'references/example.md').write_text('reference ' + text)
            return sha
        return fetch
    def test_install_update_backup_and_idempotence(self):
        r = sync_skill.sync(self.target, fetch=self.release())
        self.assertEqual(r['status'], 'installed')
        self.assertEqual(sync_skill.sync(self.target, fetch=self.release())['status'], 'up_to_date')
        r = sync_skill.sync(self.target, fetch=self.release('two', 'b'*40))
        self.assertEqual(r['status'], 'updated')
        self.assertEqual((Path(r['backup']) / 'SKILL.md').read_text(), 'version one')
        self.assertEqual((self.target / 'references/example.md').read_text(), 'reference two')
    def test_local_edit_and_new_file_preserved(self):
        sync_skill.sync(self.target, fetch=self.release())
        (self.target / 'local.md').write_text('my preferences')
        r = sync_skill.sync(self.target, fetch=self.release('two'))
        self.assertEqual(r['status'], 'local_changes')
        self.assertEqual((self.target / 'SKILL.md').read_text(), 'version one')
        self.assertIn('local.md', r['changed_files'])
    def test_network_failure_preserves_current(self):
        sync_skill.sync(self.target, fetch=self.release())
        def fail(stage):
            raise TimeoutError('offline')
        with self.assertRaises(TimeoutError):
            sync_skill.sync(self.target, fetch=fail)
        self.assertEqual((self.target / 'SKILL.md').read_text(), 'version one')
        self.assertFalse((self.target.parent / '.sps-skill-state' / sync_skill.SKILL / 'sync.lock').exists())
    def test_unmanaged_requires_adopt(self):
        self.target.mkdir(parents=True)
        (self.target / 'SKILL.md').write_text('untracked')
        self.assertEqual(sync_skill.sync(self.target, fetch=self.release())['status'], 'unmanaged')
        r = sync_skill.sync(self.target, adopt=True, fetch=self.release())
        self.assertEqual((Path(r['backup']) / 'SKILL.md').read_text(), 'untracked')
    def test_failed_replacement_rolls_back(self):
        sync_skill.sync(self.target, fetch=self.release())
        rename = Path.rename
        def fail_stage(p, target):
            if '.sps-sync-' in str(p):
                raise OSError('simulated staging failure')
            return rename(p, target)
        with patch.object(Path, 'rename', fail_stage), self.assertRaises(OSError):
            sync_skill.sync(self.target, fetch=self.release('two'))
        self.assertEqual((self.target / 'SKILL.md').read_text(), 'version one')
        self.assertEqual(sync_skill.sync(self.target, fetch=self.release())['status'], 'up_to_date')

if __name__ == '__main__':
    unittest.main()
