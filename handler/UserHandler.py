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

    def arrangeAlpha(self, row):
        users = {}
        users['firstname'] = row[0]
        users['lastname'] = row[1]
        users['phone'] = row[2]
        users['email'] = row[3]
        users['username'] = row[4]
        return users

    def arrangeBeta(self, row):
        users = {}
        users['username'] = row[0]
        users['password'] = row[1]
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

    def arrangeID(self, usrid):
        user = {}
        user['id'] = usrid[0]
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

    def insertUser(self, form):
        if len(form) != 6:
            return jsonify(ERROR="Malformed form"), 401
        else:
            fname = form['firstname']
            lname = form['lastname']
            phone = form['phone']
            email = form['email']
            username = form['username']
            password = form['password']
            if fname and lname and phone and email and username and password:
                dao = UsersDAO()
                exists = dao.check(username)
                print (exists)
                if exists:
                    new = dao.insert(fname, lname, phone, email, username, password)
                    result = self.arrangeID(new)
                    return jsonify(User=result)
                else:
                    return jsonify(ERROR='Username already exists')
            else:
                return jsonify(ERROR='After method')

    def authorize(self, form):
        if len(form) != 2:
            return jsonify(ERROR='Malformed request formed(first if)')
        else:
            username = form['username']
            password = form['password']
            if username and password:
                dao = UsersDAO()
                auth = dao.authorize(username, password)
                if auth:
                    result = self.arrange(auth)
                    return jsonify(User=result)
                else:
                    return jsonify(ERROR='Wrong Password or Username/Email')
            else:
                return jsonify(ERROR='Malformed request form(last return)')