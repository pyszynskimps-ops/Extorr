"""Publish an owner-prepared payload; never replace assets on an already published release."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import zipfile
import base64
from datetime import datetime,timezone
from catalogue import filename,update_catalogue

REPO = 'pyszynskimps-ops/Extorr'
assert os.environ.get('GITHUB_REPOSITORY') == REPO
payload = Path('payload').resolve()
plan = json.loads((payload / 'publish-plan.json').read_text())
assert 1 <= len(plan) <= 3
assert len({app['key'] for app in plan}) == len(plan)
assert {app['key'] for app in plan} <= {'1337x', 'extor', 'torrent-player'}

def gh(*args, allow_failure=False, payload=None):
    result = subprocess.run(['gh', *args], input=json.dumps(payload) if payload is not None else None, capture_output=True, text=True)
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
    assert set(expected) <= set(assets), 'Missing release assets'
    for name, digest in expected.items():
        assert assets[name]['state'] == 'uploaded'
        assert assets[name].get('digest') == 'sha256:' + digest, 'Server digest mismatch'

# Complete local verification of all selected binaries before creating/publishing anything.
for app in plan:
    assert re.fullmatch(r'(1337x|extor|torrent-player)-v[0-9]+\.[0-9]+(?:\.[0-9]+)?', app['tag'])
    assert app['tag'] == app['key'] + '-v' + app['version']
    assert len(app['assets']) == 2
    expected_names = {filename(app['key'],app['version'],device) for device in ['tv','mobile']}
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
    if not remote:
        gh('release', 'create', app['tag'], '--repo', REPO, '--target', 'main', '--draft', '--prerelease',
           '--title', app['title'] + ' ' + app['version'] + ' — Android TV i mobile', '--notes-file', str(inside(app['notes'])))
    elif remote['draft']:
        gh('release', 'edit', app['tag'], '--repo', REPO, '--target', 'main', '--notes-file', str(inside(app['notes'])))
    # Add versioned aliases without replacing any already published asset.
    remote=release(app['tag'])
    known={asset['name']:asset for asset in remote['assets']}
    paths=[inside(a['path']) for a in app['assets']]+[inside(app['checksums'])]
    for path in paths:
        previous=known.get(path.name)
        if previous:
            assert previous['digest']=='sha256:'+expected[path.name], 'Published asset differs; increment the app version'
        else:
            gh('release','upload',app['tag'],'--repo',REPO,str(path))
    attest(release(app['tag']), expected)
    if remote['draft']: staged.append(app)
    print(app['tag'] + ': staged and verified')

# Publication is the final phase, after all selected drafts and every server digest are verified.
for app in staged:
    gh('release', 'edit', app['tag'], '--repo', REPO, '--draft=false', '--prerelease', '--latest=false')
    remote = release(app['tag'])
    assert not remote['draft']
    print(app['tag'] + ': published ' + remote['html_url'])

# Every successful publication updates one public manifest; the website reads it automatically.
endpoint=f'repos/{REPO}/contents/downloads.json'
for attempt in range(3):
    file=json.loads(gh('api',endpoint+'?ref=main').stdout)
    current=json.loads(base64.b64decode(file['content']))
    public={app['tag']:release(app['tag']) for app in plan}
    updated=update_catalogue(current,plan,public,datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'))
    if updated==current:
        print('Website catalogue already current');break
    content=base64.b64encode((json.dumps(updated,indent=2)+'\n').encode()).decode()
    result=gh('api','--method','PUT',endpoint,'--input','-',allow_failure=True,payload={
        'message':'Update public downloads and publication date','sha':file['sha'],'branch':'main','content':content})
    if not result.returncode:
        print('Website catalogue and last-updated date published');break
    if '409' not in result.stderr or attempt==2:raise RuntimeError(result.stderr[:1500])
