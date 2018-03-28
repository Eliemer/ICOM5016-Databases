class UsersDAO:

    def __init__(self):
        self.users = []
        U1 = [158, 'Christian', 'Santiago', 7879582355, 'fucksgiven@example.com', 'csant', 'lolo']
        U2 = [458, 'Rjuan', 'Sanchez', 9394586251, 'givenfucks@example.com', 'rsanch', 'lola']
        U3 = [584, 'Eliemer', 'Velez', 6258849258, 'gifucksven@example.com', 'evel', ' lolu']
        U4 = [265, 'Superman', 'Kent', 7274567854, 'superman@example.com', ' superman', 'batdie']
        U5 = [854, 'Batman', 'Wayne', 8002544562, 'bigbat@example.com', 'batman1', 'batcave']
        U6 = [965, 'Batman', 'Kent', 5682541532, 'lilbat@example.com', 'batman23', 'batmobile']
        self.users.append(U1)
        self.users.append(U2)
        self.users.append(U3)
        self.users.append(U4)
        self.users.append(U5)
        self.users.append(U6)

    def getUsers(self):
        return self.users

    # Search by unique or partially unique identifiers
    def getUsersByName(self, name):
        users = []
        for u in self.users:
            if name == u[1] or name == u[1] + u[2]:
                users.append(u)
        return users

    def getUserById(self, usrid):
        users = []
        for u in self.users:
            if usrid == u[0]:
                users.append(u)
        return users

    def getUserByEmail(self, email):
        users = []
        for u in self.users:
            if email == u[4]:
                users.append(u)
        return users

    def getUserByUserName(self, username):
        users = []
        for u in self.users:
            if username == u[5]:
                users.append(u)
        return users

    # Getters
    def getUserName(self, uid):
        user = []
        for u in self.users:
            if uid == u[0]:
                user.append(u)
        return user

    def getUserLastName(self, gid):
        user = []
        for u in self.users:
            if gid == u[0]:
                user.append(u)
        return user

    def getUserPhone(self, gid):
        phone = []
        for p in self.users:
            if gid == p[0]:
                phone.append(p)
        return phone

    def loginUserNameAndPasswod(self, username, password):
        for u in getUserByUserName(username):
            return password == u[6]
