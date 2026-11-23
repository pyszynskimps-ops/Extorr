import json
import unittest
from types import SimpleNamespace
from release_lookup import ReleaseLookup

class ReleaseLookupTest(unittest.TestCase):
    def test_created_draft_is_read_by_id_even_when_listing_is_stale(self):
        calls=[]
        def gh(*args,**kwargs):
            calls.append((args,kwargs))
            if '--method' in args:
                self.assertEqual('POST',args[2])
                self.assertEqual('A release note',kwargs['payload']['body'])
                self.assertTrue(kwargs['payload']['draft'])
                return SimpleNamespace(stdout=json.dumps(dict(id=42,tag_name='app-v2.23',draft=True)))
            if args[-1].endswith('?per_page=100'):return SimpleNamespace(stdout='[]')
            self.assertEqual('repos/owner/app/releases/42',args[-1])
            return SimpleNamespace(stdout=json.dumps(dict(id=42,tag_name='app-v2.23',draft=True,assets=[dict(name='tv.apk')])))
        lookup=ReleaseLookup(gh,'owner/app')
        self.assertIsNone(lookup.find('app-v2.23'))
        lookup.create_draft('app-v2.23','Title','A release note')
        self.assertEqual('tv.apk',lookup.find('app-v2.23')['assets'][0]['name'])
        self.assertEqual(1,sum(args[-1].endswith('?per_page=100') for args,_ in calls))

    def test_existing_release_uses_fresh_record_for_assets_and_publication_state(self):
        reads=0
        def gh(*args,**kwargs):
            nonlocal reads
            if args[-1].endswith('?per_page=100'):
                return SimpleNamespace(stdout=json.dumps([dict(id=12,tag_name='app-v2.23',draft=True,assets=[])]))
            reads+=1
            return SimpleNamespace(stdout=json.dumps(dict(id=12,tag_name='app-v2.23',draft=reads==1,assets=[dict(name='mobile.apk')])))
        lookup=ReleaseLookup(gh,'owner/app')
        self.assertTrue(lookup.find('app-v2.23')['draft'])
        current=lookup.find('app-v2.23')
        self.assertFalse(current['draft']);self.assertEqual('mobile.apk',current['assets'][0]['name'])

if __name__=='__main__':unittest.main()
