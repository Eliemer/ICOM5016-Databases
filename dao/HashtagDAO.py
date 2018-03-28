from dao.MessagesDAO import MessagesDAO


class HashtagDAO:
    def __init__(self):
        self.hashtags = []
        messages = MessagesDAO().getMessages()
        tmp = []
        for m in messages:
            tmp.append(m[2].split('#'))
            self.hashtags.append(tmp)


    def getHashtags(self):
        return self.hashtags







