"""Use stable release IDs after writes; release listings can lag newly created drafts."""
import json

class ReleaseLookup:
    def __init__(self, gh, repository):
        self.gh=gh
        self.repository=repository
        self.ids={}

    def find(self, tag):
        if tag not in self.ids:
            releases=json.loads(self.gh('api',f'repos/{self.repository}/releases?per_page=100').stdout)
            found=next((release for release in releases if release['tag_name']==tag),None)
            if found is None:return None
            self.ids[tag]=found['id']
        return json.loads(self.gh('api',f'repos/{self.repository}/releases/{self.ids[tag]}').stdout)

    def create_draft(self, tag, title, notes):
        record=json.loads(self.gh('api','--method','POST',f'repos/{self.repository}/releases','--input','-',payload={
            'tag_name':tag,'target_commitish':'main','name':title,'body':notes,'draft':True,'prerelease':True}).stdout)
        assert record['tag_name']==tag and record['draft']
        self.ids[tag]=record['id']
        return record
