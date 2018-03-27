from dao.UserDAO import UsersDAO
from flask import *


class UserHandler:

    def mapAllToDict(self, row):
        users = []
        users['user_id'] = row[0]
        users['first_name'] = row[1]
        users['last_name'] = row[2]
        users['phone'] = row[3]
        users['email'] = row[4]
        return users

    def mapIDToDict(self, row):
        uid = []
        uid['user_id'] = row
        return uid

    def mapFirstNameToDict(self, row):
        fname = []
        fname['first_name'] = row
        return fname

    def mapLastNameToDict(self, row):
        lname = []
        lname['last_name'] = row
        return lname

    def mapPhoneToDict(self, row):
        phone =[]
        phone['phone'] = row
        return phone

    def mapEmailToDict(self, row):
        email = []
        email['email'] = row
        return email

    def getAllUsers(self):
        dao = UsersDAO()
        result = dao.getUsers()
        users = []
        if result is None:
            return jsonify(ERROR='No users found')
        for i in result:
            users.append(self.mapAllToDict(i))
        return jsonify(Users=users)

    def getAllUserIDs(self):
        dao = UsersDAO()
        result = dao.getUsers()
        mapped = []
        if result is None:
            return jsonify(ERROR='No users found')
        for i in result:
            mapped.append(self.mapIDToDict(i))
        return jsonify(Users=mapped)

    def getAllUserNames(self):
        dao = UsersDAO()
        result = dao.getUsers()
        mapped = []
        if result is None:
            return jsonify(ERROR='No users found')
        for i in result:
            mapped.append(self.mapFirstNameToDict(i), self.mapLastNameToDict(i))
        return jsonify(Users=mapped)

    def getAllUserPhones(self):
        dao = UsersDAO()
        result = dao.getUsers()
        mapped = []
        if result is None:
            return jsonify(ERROR='No users found')
        for i in result:
            mapped.append(self.mapPhoneToDict(i))
        return jsonify(Users=mapped)

    def getAllUserEmails(self):
        dao = UsersDAO()
        result = dao.getUsers()
        mapped = []
        if result is None:
            return jsonify(ERROR='No users found')
        for i in result:
            mapped.append(self.mapEmailToDict(i))
        return jsonify(Users=mapped)

    def getUserByName(self, name):
        dao = UsersDAO()
        result = dao.getUsersByName(name)
        mapped =[]
        if result is None:
            return jsonify(ERROR="No User Found")
        for r in result:
            mapped.append(self.mapAllToDict(r))
        return jsonify(Users=mapped)

    def getUserById(self, uid):
        dao = UsersDAO()
        result = dao.getUserById(uid)
        mapped = []
        if result is None:
            return jsonify(ERROR='No User found by that ID')
        for r in result:
            mapped.append(self.mapAllToDict(r))
        return jsonify(Users=mapped)

    def getUserByEmail(self, email):
        dao = UsersDAO()
        result = dao.getUserByEmail(email)
        mapped = []
        if result is None:
            return jsonify(ERROR='No User found by that email')
        for r in result:
            mapped.append(self.mapAllToDict(r))
        return jsonify(Users=mapped)

    def getUserID(self, name):
        dao = UsersDAO()
        result = dao.getUsersByName(name)
        mapped = []
        if result is None:
            return jsonify(ERROR='No User found by that name')
        for r in result:
            mapped.append(self.mapIDToDict(r))
        return jsonify(Groups=mapped)

    def getUserName(self, uid):
        dao = UsersDAO()
        result = dao.getUsersByID(uid)
        mapped = []
        if result is None:
            return jsonify(ERROR='No User found by that ID')
        for r in result:
            mapped.append(self.mapFirstNameToDict(r), self.mapLastNameToDict(r))
        return jsonify(Groups=mapped)

    def getUserLastName(self, uid):
        dao = UsersDAO()
        result = dao.getUsersByName(uid)
        mapped = []
        if result is None:
            return jsonify(ERROR='No User found by that ID')
        for r in result:
            mapped.append(self.mapLastNameToDict(r))
        return jsonify(Groups=mapped)

    def getUserEmail(self, uid):
        dao = UsersDAO()
        result = dao.getUsersByName(uid)
        mapped = []
        if result is None:
            return jsonify(ERROR='No User found by that ID')
        for r in result:
            mapped.append(self.mapEmailToDict(r))
        return jsonify(Groups=mapped)

    def getUserPhone(self, uid):
        dao = UsersDAO()
        result = dao.getUsersByName(uid)
        mapped = []
        if result is None:
            return jsonify(ERROR='No User found by that ID')
        for r in result:
            mapped.append(self.mapPhoneToDict(r))
        return jsonify(Groups=mapped)
