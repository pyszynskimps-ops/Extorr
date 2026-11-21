"""Publish an owner-prepared payload; never replace assets on an already published release."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import zipfile

REPO = 'pyszynskimps-ops/Extorr'
assert os.environ.get('GITHUB_REPOSITORY') == REPO
payload = Path('payload').resolve()
plan = json.loads((payload / 'publish-plan.json').read_text())
assert {app['key'] for app in plan} == {'1337x', 'extor'} and len(plan) == 2

def gh(*args, allow_failure=False):
    result = subprocess.run(['gh', *args], capture_output=True, text=True)
    if result.returncode and not allow_failure:
        raise RuntimeError(result.stderr[:1500])
    return result

def releases():
    return json.loads(gh('api', f'repos/{REPO}/releases?per_page=100').stdout)

def release(tag):
    return next((r for r in releases() if r['tag_name'] == tag), None)

def inside(relative):
    path = (payload / relative).resolve()
    assert path.is_file() and payload in path.parents
    return path

def attest(remote, expected):
    assets = {a['name']: a for a in remote['assets']}
    assert set(assets) == set(expected), 'Unexpected release asset set'
    for name, digest in expected.items():
        assert assets[name]['state'] == 'uploaded'
        assert assets[name].get('digest') == 'sha256:' + digest, 'Server digest mismatch'

# Complete local verification of all four binaries before creating/publishing anything.
for app in plan:
    assert re.fullmatch(r'(1337x|extor)-v[0-9]+\.[0-9]+', app['tag'])
    assert app['tag'] == app['key'] + '-v' + app['version']
    assert len(app['assets']) == 2
    expected_names = {app['key'] + '-android-tv-armeabi-v7a.apk', app['key'] + '-android-mobile-arm64-v8a.apk'}
    assert {a['name'] for a in app['assets']} == expected_names
    for asset in app['assets']:
        path = inside(asset['path'])
        assert path.name == asset['name'] and path.stat().st_size == asset['size']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == asset['sha256']
        with zipfile.ZipFile(path) as apk:
            assert apk.testzip() is None
            assert 'AndroidManifest.xml' in apk.namelist() and 'classes.dex' in apk.namelist()
            abis = {name.split('/')[1] for name in apk.namelist() if name.startswith('lib/') and name.endswith('.so')}
            assert abis == {asset['abi']}
    checksums = inside(app['checksums'])
    assert checksums.read_text() == ''.join(a['sha256'] + '  ' + a['name'] + '\n' for a in app['assets'])
    inside(app['notes'])

staged = []
for app in plan:
    remote = release(app['tag'])
    expected = {a['name']: a['sha256'] for a in app['assets']}
    expected[Path(app['checksums']).name] = hashlib.sha256(inside(app['checksums']).read_bytes()).hexdigest()
    if remote and not remote['draft']:
        attest(remote, expected)
        continue
    if not remote:
        gh('release', 'create', app['tag'], '--repo', REPO, '--target', 'main', '--draft', '--prerelease',
           '--title', app['title'] + ' ' + app['version'] + ' — Android TV i mobile', '--notes-file', str(inside(app['notes'])))
    else:
        gh('release', 'edit', app['tag'], '--repo', REPO, '--target', 'main', '--notes-file', str(inside(app['notes'])))
    gh('release', 'upload', app['tag'], '--repo', REPO, '--clobber',
       *[str(inside(a['path'])) for a in app['assets']], str(inside(app['checksums'])))
    attest(release(app['tag']), expected)
    staged.append(app)
    print(app['tag'] + ': staged and verified')

# Publication is the final phase, after both drafts and every server digest are verified.
for app in staged:
    gh('release', 'edit', app['tag'], '--repo', REPO, '--draft=false', '--prerelease', '--latest=false')
    remote = release(app['tag'])
    assert not remote['draft']
    print(app['tag'] + ': published ' + remote['html_url'])
