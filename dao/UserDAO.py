from config.db_config import pg_config
import psycopg2


class UsersDAO:

    def __init__(self):
        connUrl = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                     pg_config['user'],
                                                     pg_config['password'])
        self.connection = psycopg2._connect(connUrl)

    def getUsers(self):
        cursor = self.connection.cursor()
        query = "select * from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Search by unique or partially unique identifiers
    def getUsersByName(self, username):
        cursor = self.connection.cursor()
        query = "select * from Users where uusername=%s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserById(self, usrid):
        cursor = self.connection.cursor()
        query = "select * from Users where usrid=%s;"
        cursor.execute(query, (usrid,))
        result = cursor.fetchone()
        return result

    def getUserByEmail(self, email):
        cursor = self.connection.cursor()
        query = "select * from Users where email=%s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def getUsersEmails(self):
        cursor = self.connection.cursor()
        query = "select ufirstname, ulastname,  email from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUsername(self, username):
        users = []
        for u in self.users:
            if username == u[5]:
                users.append(u)
        return users

    # Getters for each attribute of the user
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
