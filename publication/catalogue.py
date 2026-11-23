"""Versioned filenames and the public catalogue consumed by the download website."""
from copy import deepcopy
import re

APPS={'torrent-player','extor','1337x'}
DEVICES={'tv':'armeabi-v7a','mobile':'arm64-v8a'}
REPOSITORY='pyszynskimps-ops/Extorr'
BASE=f'https://github.com/{REPOSITORY}/releases/'

def filename(app,version,device):
    assert app in APPS and device in DEVICES
    assert re.fullmatch(r'[0-9]+\.[0-9]+(?:\.[0-9]+)?',version),'Invalid version'
    return f'{app}-v{version}-android-{device}-{DEVICES[device]}.apk'

def update_catalogue(current,plan,releases,now):
    result=deepcopy(current)
    changed=False
    for app in plan:
        key=app['key'];version=app['version'];previous=result['applications'].get(key,{})
        if tuple(map(int,previous.get('version','0.0').split('.')))>tuple(map(int,version.split('.'))):
            continue  # Retrying an older release must never roll back website links.
        release=releases[app['tag']]
        assert not release['draft']
        assets={}
        for asset in app['assets']:
            device=next(d for d,abi in DEVICES.items() if asset['abi']==abi)
            name=filename(key,version,device)
            assert name==asset['name']
            assets[device]={'url':BASE+'download/'+app['tag']+'/'+name,'filename':name,'abi':asset['abi'],'size':asset['size'],'sha256':asset['sha256']}
        value={k:v for k,v in previous.items() if k!='updated_at'}
        value.update(version=version,release_url=release['html_url'],prerelease=release['prerelease'],
                     published_at=release['published_at'],assets=assets)
        comparable={k:v for k,v in previous.items() if k!='updated_at'}
        if comparable!=value:
            value['updated_at']=now
            result['applications'][key]=value
            changed=True
    if changed:
        result['schema_version']=2
        result['updated_at']=now
    return result
