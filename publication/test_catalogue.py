import unittest
from catalogue import filename,update_catalogue

class CatalogueTest(unittest.TestCase):
    def test_versioned_names_and_invalid_input(self):
        self.assertEqual('torrent-player-v2.22-android-tv-armeabi-v7a.apk',filename('torrent-player','2.22','tv'))
        self.assertEqual('extor-v1.04-android-mobile-arm64-v8a.apk',filename('extor','1.04','mobile'))
        for value in ['../2.22','2.22.apk','latest','2/22']:
            with self.assertRaises(AssertionError):filename('torrent-player',value,'tv')
    def test_publication_updates_links_and_date_once_and_preserves_other_apps(self):
        current={'schema_version':1,'applications':{'extor':{'version':'1.04'}}}
        app={'key':'torrent-player','version':'2.22','tag':'torrent-player-v2.22','assets':[
            {'name':filename('torrent-player','2.22',d),'abi':abi,'size':1234,'sha256':'a'*64} for d,abi in [('tv','armeabi-v7a'),('mobile','arm64-v8a')]]}
        releases={app['tag']:{'draft':False,'prerelease':True,'html_url':'https://github.com/pyszynskimps-ops/Extorr/releases/tag/'+app['tag'],'published_at':'2026-11-23T14:55:00Z'}}
        updated=update_catalogue(current,[app],releases,'2026-11-23T15:30:00Z')
        self.assertEqual(current['applications']['extor'],updated['applications']['extor'])
        self.assertEqual('2026-11-23T15:30:00Z',updated['updated_at'])
        self.assertIn('v2.22',updated['applications']['torrent-player']['assets']['tv']['filename'])
        self.assertEqual(updated,update_catalogue(updated,[app],releases,'2026-11-24T00:00:00Z'))
        updated['applications']['torrent-player']['version']='2.23'
        self.assertEqual(updated,update_catalogue(updated,[app],releases,'2026-11-24T00:00:00Z'))

if __name__=='__main__':unittest.main()
