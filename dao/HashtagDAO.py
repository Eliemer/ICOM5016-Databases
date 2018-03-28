from dao.MessagesDAO import MessagesDAO

class HashtagDAO:
    def _init_(self):
        self.hashtags = []
        tmp = []
        messages = MessagesDAO.getMessages()
        regex = '\# '
        for m in messages:
            tmp = m[2].split(regex)
            self.hashtags.append(tmp[1])






