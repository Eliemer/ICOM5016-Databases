from config.db_config import pg_config, dbconnect
import psycopg2
import os


class UsersDAO:
    def __init__(self):
        # Uncomment for heroku use
        # DATABASE_URL = os.environ['HEROKU_POSTGRESQL_PINK_URL']
        #
        # self.connection = psycopg2._connect(DATABASE_URL)

        # Uncomment for local use
        connUrl = dbconnect
        self.connection = psycopg2._connect(connUrl)

    def getUsers(self):
        cursor = self.connection.cursor()
        query = "select * from Users order by usrid;"
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

    def insert(self, fname, lname, phone, email, username, password):
        cursor = self.connection.cursor()
        query = "insert into users (ufirstname, ulastname, uphone, email, uusername, upassword) VALUES " \
                "(%s, %s, %s, %s, %s, crypt(%s, gen_salt('bf', 8))) returning usrid;"
        cursor.execute(query, (fname, lname, phone, email, username, password,))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    def authorize(self, username, password):
        cursor = self.connection.cursor()
        query = "select * from users where upassword = crypt(%s, upassword) and (email=%s or uusername=%s);"
        cursor.execute(query, (password, username, username,))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    def check(self, username):
        cursor = self.connection.cursor()
        query = "select exists (select false from users where uusername=%s);"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    # def getUserByEmail(self, email):
    #     cursor = self.connection.cursor()
    #     query = "select * from Users where email=%s;"
    #     cursor.execute(query, (email,))
    #     result = cursor.fetchone()
    #     return result

    # def getUsersEmails(self):
    #     cursor = self.connection.cursor()
    #     query = "select ufirstname, ulastname,  email from Users;"
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getUserByUsername(self, username):
        users = []
        for u in self.users:
            if username == u[5]:
                users.append(u)
        return users

    # Getters for each attribute of the user
    # def getUserName(self, uid):
    #     user = []
    #     for u in self.users:
    #         if uid == u[0]:
    #             user.append(u)
    #     return user
    #
    # def getUserLastName(self, gid):
    #     user = []
    #     for u in self.users:
    #         if gid == u[0]:
    #             user.append(u)
    #     return user
    #
    # def getUserPhone(self, gid):
    #     phone = []
    #     for p in self.users:
    #         if gid == p[0]:
    #             phone.append(p)
    #     return phone
    #
    # def loginUserNameAndPasswod(self, username, password):
    #     for u in getUserByUserName(username):
    #         return password == u[6]
