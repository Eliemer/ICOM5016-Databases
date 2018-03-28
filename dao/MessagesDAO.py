from dao.UserDAO import UsersDAO
from dao.GroupChatDAO import GroupChatDAO


class MessagesDAO:
    def __init__(self):
        self.messages = []
        m1 = [1,
              UsersDAO().users[0][0],
              GroupChatDAO().groups[0][0],
              '03-18-2018 7:13pm',
              'Hello World #notexample']
        m2 = [2,
              UsersDAO().users[1][0],
              GroupChatDAO().groups[0][0],
              '03-18-2018 7:13pm',
              'Sup? #notexample']
        m3 = [3,
              UsersDAO().users[2][0],
              GroupChatDAO().groups[0][0],
              '03-18-2018 7:14pm',
              'How you doin?']
        m4 = [4,
              UsersDAO().users[3][0],
              GroupChatDAO().groups[0][0],
              '03-18-2018 7:18pm',
              'Bye World']
        m5 = [5, UsersDAO().users[0][0],
              GroupChatDAO().groups[0],
              '03-18-2018 7:22pm',
              'ByeBye']
        m6 = [6,
              UsersDAO().users[0][0],
              GroupChatDAO().groups[0][0],
              '03-18-2018 7:23pm',
              'Hello Hell']
        m7 = [7,
              UsersDAO().users[0][0],
              GroupChatDAO().groups[0][0],
              '03-18-2018 7:23pm',
              'DB is the best']
        m8 = [8,
              UsersDAO().users[0][0],
              GroupChatDAO().groups[0][0],
              '03-18-2018 7:24pm',
              'Python sucks big time #example']
        m9 = [9, UsersDAO().users[0][0],
              GroupChatDAO().groups[0][0],
              '03-18-2018 7:28pm',
              'See you tomorrow #example']

        self.messages.append(m1)
        self.messages.append(m2)
        self.messages.append(m3)
        self.messages.append(m4)
        self.messages.append(m5)
        self.messages.append(m6)
        self.messages.append(m7)
        self.messages.append(m8)
        self.messages.append(m9)

    def getMessages(self):
        return self.messages

    def getUserMessagebyId(self, usrid):
        result = []
        for i in self.messages:
            if usrid == i[0]:
                result.append(i)
        return result

    def getHashtags(self):
        result = []
        for m in self.messages:
            h = m[2].split('#')
            if len(h) > 1:
                result.append('#' + h[1])

        return result
