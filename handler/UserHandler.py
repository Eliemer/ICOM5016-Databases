from dao.UserDAO import UsersDAO
from flask import *


class UserHandler:

    def arrange(self, row):
        users = {}
        users['usrid'] = row[0]
        users['firstname'] = row[1]
        users['lastname'] = row[2]
        users['phone'] = row[3]
        users['email'] = row[4]
        return users

    def getUsers(self):
        dao = UsersDAO()
        result = dao.getUsers()
        users = []
        for i in result:
            users.append(self.arrange(i))
        return jsonify(Users=users)

    def getUsersByName(self, name):
        dao = UsersDAO()
        result = dao.getUsersByName(name)
        if result is None:
            return jsonify(ERROR="No User Found")
        return jsonify(Users=result)

    def getUserById(self, usrid):
        dao = UsersDAO()
        result = dao.getUserById(usrid)
        if result is None:
            return jsonify(ERROR='No User found by that ID')
        return jsonify(Users=result)

    def getUsersEmails(self):
        dao = UsersDAO()
        result = dao.getUsersEmails()
        return jsonify(Messages=result)
