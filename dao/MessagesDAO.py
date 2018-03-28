from dao.UserDAO import UsersDAO


class MessagesDAO:
    def __init__(self):
        self.messages = []
        # m = [id, name, content, likes, dislikes]
        m1 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'Hello World',4,5]
        m2 = [UsersDAO().users[1][0], UsersDAO().users[1][1], 'Sup?',5,2]
        m3 = [UsersDAO().users[2][0], UsersDAO().users[2][1], 'How you doin?',5,3]
        m4 = [UsersDAO().users[3][0], UsersDAO().users[3][1], 'Bye World',4,8]
        m5 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'ByeBye',0,0]
        m6 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'Hello Hell',9,8]
        m7 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'DB is the best',6,0]
        m8 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'Python sucks big time',0,4]
        m9 = [UsersDAO().users[0][0], UsersDAO().users[0][1], 'See you tomorrow',8,7]

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
