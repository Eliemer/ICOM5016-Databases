from dao.UserDAO import UsersDAO
from flask import jsonify


class UserHandler:

    def arrange(self, row):
        users = {}
        users['usrid'] = row[0]
        users['firstname'] = row[1]
        users['lastname'] = row[2]
        users['phone'] = row[3]
        users['email'] = row[4]
        users['username'] = row[5]
        return users

    def arrangeUserID(self, row):
        users = {}
        users['usrid'] = row[0]
        return users

    def arrangeFirstName(self, fname):
        name = {}
        name['firstname'] = fname[1]
        return name

    def arrangeLastName(self, lname):
        name = {}
        name['lastname'] = lname[2]
        return name

    def arrangePhone(self, phone):
        phones = {}
        phones['phone number'] = phone[3]
        return phones

    def arrangeEmails(self, row):
        emails = {}
        emails['email'] = row
        return emails

    def arrangeUserName(self, usrname):
        user = {}
        user['username'] = usrname[5]
        return user

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
        if result:
            for r in result:
                mapp = self.arrange(r)
            return jsonify(Users=mapp)
        return jsonify(ERROR="No User Found")

    def getUserById(self, usrid):
        dao = UsersDAO()
        result = dao.getUserById(usrid)
        if result is None:
            return jsonify(ERROR='No User found by that ID')
        mapp = []
        for r in result:
            mapp.append(self.arrange(r))
        return jsonify(Users=mapp)

    def getUserByUsername(self, username):
        dao = UsersDAO()
        result = dao.getUserByUsername(username)
        users = []
        if result:
            for u in result:
                users.append(self.arrange(u))
            return jsonify(User=users)
        else:
            return jsonify(ERROR='Username doesn\'t exists')

    def getUsersEmails(self):
        dao = UsersDAO()
        result = dao.getUsersEmails()
        mapp = []
        for r in result:
            mapp.append(self.arrangeEmails(r))
        return jsonify(Users=mapp)

    def getUserByPhone(self, phone):
        dao = UsersDAO()
        result = dao.getUserByPhone(phone)
        mapp = []
        for r in result:
            mapp.append(self.arrangePhone(r))
        return jsonify(Phone=mapp)
