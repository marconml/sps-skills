#!/usr/bin/env python3
"""Install/update the shared skill; standard library only, no report data touched."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import time
import urllib.request
import zipfile

REPO = 'marconml/sps-skills'
SKILL = 'chief-editor-review'
REF = 'dev'

def inventory(root):
    result = {}
    for p in sorted(root.rglob('*')):
        if '__pycache__' in p.parts or p.suffix == '.pyc':
            continue
        if p.is_symlink():
            raise ValueError('Symlink in installed skill: ' + str(p.relative_to(root)))
        if p.is_file():
            result[p.relative_to(root).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result

def download(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'SPS-skill-sync/1', 'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read(30 * 1024 * 1024 + 1)
    if len(payload) > 30 * 1024 * 1024:
        raise ValueError('Download exceeds 30 MB limit')
    return payload

def fetch_release(stage):
    meta = json.loads(download(f'https://api.github.com/repos/{REPO}/commits/{REF}'))
    sha = meta['sha']
    if len(sha) != 40 or any(c not in '0123456789abcdef' for c in sha):
        raise ValueError('Invalid release SHA')
    archive = zipfile.ZipFile(io.BytesIO(download(f'https://codeload.github.com/{REPO}/zip/{sha}')))
    total = 0
    for item in archive.infolist():
        parts = PurePosixPath(item.filename).parts
        if len(parts) < 3 or parts[1] != SKILL or item.is_dir():
            continue
        relative = PurePosixPath(*parts[2:])
        if '..' in relative.parts or relative.is_absolute() or (item.external_attr >> 16) & 0o170000 == 0o120000:
            raise ValueError('Unsafe archive member')
        total += item.file_size
        if total > 20 * 1024 * 1024:
            raise ValueError('Skill exceeds 20 MB limit')
        target = stage.joinpath(*relative.parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(archive.read(item))
    if not (stage / 'SKILL.md').is_file() or not (stage / 'scripts/sync_skill.py').is_file():
        raise ValueError('Incomplete shared release')
    return sha

def sync(target, adopt=False, fetch=fetch_release):
    target = Path(target).expanduser().absolute()
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_symlink():
        raise ValueError('Target is a symlink')
    state_dir = target.parent / '.sps-skill-state' / SKILL
    state_dir.mkdir(parents=True, exist_ok=True)
    state_file = state_dir / 'installed.json'
    lock = state_dir / 'sync.lock'
    try:
        fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        return {'status': 'deferred', 'reason': 'Another sync is running; if a prior process crashed, remove its stale lock after checking.'}
    os.close(fd)
    try:
        current = inventory(target) if target.exists() else {}
        saved = json.loads(state_file.read_text()) if state_file.exists() else None
        if saved and current != saved['files']:
            changed = sorted(k for k in set(current) | set(saved['files']) if current.get(k) != saved['files'].get(k))
            return {'status': 'local_changes', 'changed_files': changed, 'installed_commit': saved['commit'], 'reason': 'Preserved local files; review differences before replacing.'}
        with tempfile.TemporaryDirectory(prefix='.sps-sync-', dir=target.parent) as tmp:
            stage = Path(tmp) / SKILL
            stage.mkdir()
            sha = fetch(stage)
            incoming = inventory(stage)
            if current and not saved and current != incoming and not adopt:
                return {'status': 'unmanaged', 'reason': 'Existing install has no tracked baseline; preserved. Use --adopt only after approving its replacement.'}
            if current == incoming:
                receipt = {'commit': sha, 'files': incoming, 'repository': REPO, 'ref': REF}
                state_file.write_text(json.dumps(receipt, indent=2))
                return {'status': 'up_to_date', 'installed_commit': sha, 'repository': REPO, 'ref': REF}
            backup = None
            if target.exists():
                backup = state_dir / ('backup-' + time.strftime('%Y%m%d-%H%M%S') + '-' + str(time.time_ns()))
                target.rename(backup)
            try:
                stage.rename(target)
                receipt = {'commit': sha, 'files': incoming, 'repository': REPO, 'ref': REF}
                temp_state = state_dir / 'installed.tmp'
                temp_state.write_text(json.dumps(receipt, indent=2))
                temp_state.replace(state_file)
            except Exception:
                if target.exists():
                    shutil.rmtree(target)
                if backup:
                    backup.rename(target)
                raise
            return {'status': 'updated' if backup else 'installed', 'installed_commit': sha, 'backup': str(backup) if backup else None, 'repository': REPO, 'ref': REF}
    finally:
        lock.unlink(missing_ok=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills' / SKILL)
    parser.add_argument('--adopt', action='store_true', help='Explicitly replace an untracked existing install after backing it up.')
    args = parser.parse_args()
    try:
        result = sync(args.target, args.adopt)
    except Exception as exc:
        result = {'status': 'unavailable', 'reason': str(exc), 'instruction': 'Continue with existing installed version if available.'}
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
