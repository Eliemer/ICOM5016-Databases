from flask import *
from dao.HashtagDAO import *


class HashtagHandler:
    def sort(self, row):
        hashtags = {}
        hashtags['hashtag'] = row[1]
        return hashtags

    def getHashtags(self):
        dao = HashtagDAO()
        result = dao.getHashtags()
        mapp = []
        for r in result:
            mapp.append(self.sort(r))
        return jsonify(HashTag=mapp)
