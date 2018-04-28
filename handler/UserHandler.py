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

    def arrange2(self, row):
        users ={}
        users['Name'] = row[0]
        users['Lastname'] = row[1]
        users['Email'] = row[2]
        return users

    def getUsers(self):
        dao = UsersDAO()
        result = dao.getUsers()
        users = []
        for i in result:
            users.append(self.arrange(i))
        return jsonify(Users=users)

    def getUsersByUsername(self, username):
        dao = UsersDAO()
        result = dao.getUsersByName(username)
        if result:
            user = self.arrange(result)
            return jsonify(Users=user)
        return jsonify(ERROR="User doesn\'t exists")

    def getUserById(self, usrid):
        dao = UsersDAO()
        result = dao.getUserById(usrid)
        if result:
            user = self.arrange(result)
            return jsonify(User=user)
        return jsonify(ERROR='User doesn\'t exists')

    def getUserByName(self, username):
        dao = UsersDAO()
        result = dao.getUserByUsername(username)
        if result:
            user = self.arrange(result)
            return jsonify(User=user)
        else:
            return jsonify(ERROR='User doesn\'t exists')

    def getUsersEmails(self):
        dao = UsersDAO()
        result = dao.getUsersEmails()
        users = []
        for r in result:
            users.append(self.arrange2(r))
        return jsonify(Users=users)

    def getUserByPhone(self, phone):
        dao = UsersDAO()
        result = dao.getUserByPhone(phone)
        mapp = []
        for r in result:
            mapp.append(self.arrangePhone(r))
        return jsonify(Phone=mapp)
