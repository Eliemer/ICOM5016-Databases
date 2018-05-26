from flask import *
from dao.HashtagDAO import *
from handler.MessagesHandler import *


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

    def getMessagesWithHashtags(self, form):
        if len(form) != 1:
            return jsonify(ERROR='Error in form')
        else:
            hashtag = form['hashtag']
            mess = []
            if hashtag:
                result = MessagesHandler().getMessages()
                for r in result:
                    content = r['content']
                    if hashtag in content:
                        mess.append(r)
                return jsonify(Messages=mess)
            else:
                return jsonify(ERROR='Empty form')
