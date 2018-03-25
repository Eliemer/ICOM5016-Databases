from dao.UserDAO import UsersDAO


class MessagesDAO:
    def __init__(self):
        self.messages = []
        m1 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'Hello World']
        m2 = [UsersDAO().users[1][0], UsersDAO().users[1][1], 'Sup?']
        m3 = [UsersDAO().users[2][0], UsersDAO().users[2][1], 'How you doin?']
        m4 = [UsersDAO().users[3][0], UsersDAO().users[3][1], 'Bye World']
        m5 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'ByeBye']
        m6 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'Hello Hell']
        m7 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'DB is the best']
        m8 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'Python sucks big time']
        m9 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'See you tomorrow']

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
