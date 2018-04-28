from dao.UserDAO import *
from handler.UserHandler import *
import psycopg2


class GroupChatDAO:

    def __init__(self):
        connUrl = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                     pg_config['user'],
                                                     pg_config['password'])
        self.connection = psycopg2._connect(connUrl)

    def getGroups(self):
        cursor = self.connection.cursor()
        query = "select groupid, groupname, ufirstname, ulastname, date_created from groupchats " \
                "natural inner join members natural inner join users where admind=usrid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupByName(self, name):
        cursor = self.connection.cursor()
        query = "select * from Groupchats where groupname=%s;"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        return result

    def getGroupByID(self, gid):
        cursor = self.connection.cursor()
        query = "select ufirstname, ulastname, content, groupname " \
                "from groupchats natural inner join messages natural inner join members natural inner join users" \
                " where groupid=%s;"
        cursor.execute(query, (gid,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getGroupContent(self, name):
        cursor = self.connection.cursor()
        query = "select ufirstname, ulastname, content, groupname from users " \
                "natural inner join members natural inner join messages natural inner join groupchats where groupname=%s;"
        cursor.execute(query, (name, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # I think this is unnecessary getters, should delete them...
    def getGroupAdmin(self, gid):
        admin = []
        for g in self.groups:
            if gid == g[2]:
                admin.append(g)
        return admin

    def getGroupDate(self, gid):
        date = []
        for g in self.groups:
            if gid == g[0]:
                date.append(g[3])
        return date

    def getUsersInGroup(self, gid):
        cursor = self.connection.cursor()
        query = "select ufirstname, ulastname from groupchats natural inner join members natural inner join users " \
                "where groupid=%s;"
        cursor.execute(query, (gid,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserGroupchats(self, usrid):
        cursor = self.connection.cursor()
        query = "select * from groupchats natural inner join members where usrid=%s"
        cursor.execute(query, (usrid,))
        result = []
        for r in cursor:
            result.append(r)
        return result


