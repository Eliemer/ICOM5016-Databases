from dao.UserDAO import *
from config.db_config import *
from handler.UserHandler import *
import psycopg2
import os


class GroupChatDAO:

    def __init__(self):
        # DATABASE_URL = os.environ['HEROKU_POSTGRESQL_PINK_URL']
        #
        # self.connection = psycopg2._connect(DATABASE_URL)

        connUrl = dbconnect
        self.connection = psycopg2._connect(connUrl)

    def getGroups(self):
        cursor = self.connection.cursor()
        query = "select groupid, groupname, ufirstname, ulastname, date_created from groupchats " \
                "natural inner join users where admind=usrid;"
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
        cursor = self.connection.cursor()
        query = "select * from users natural inner join groupchats where groupid = %s and admind=usrid;"
        cursor.execute(query, (gid,))
        result = []
        for r in cursor:
            result.append(r)
        return result

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
        query = "select * from groupchats natural inner join members where usrid=%s and show=TRUE;"
        cursor.execute(query, (usrid,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserGroupContent(self, usrid, groupname):
        cursor = self.connection.cursor()
        query = "with all_messages as (select * from messages natural inner join groupchats natural inner join users " \
                "inner join members using(groupid) where groupname = %s and members.usrid=%s)," \
                " all_likes as (select count(*) as l, messageid from likes group by messageid), " \
                "all_dislikes as (select count(*) as dl, messageid from dislike group by messageid) " \
                "select messageid, content, ufirstname, ulastname, coalesce(l, 0) as likes, coalesce(dl, 0) as dislikes from all_likes " \
                "right outer join all_messages left outer join all_dislikes using(messageid) using(messageid) order by date_sent desc;"
        cursor.execute(query, (groupname, usrid,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUGMLikes(self, usrid, groupname):
        cursor = self.connection.cursor()
        query = "select count(*), messageid from likes inner join (select * from messages natural inner join groupchats natural inner join users " \
                      "inner join members using(groupid) where groupname = %s and members.usrid=%s) as MG using(messageid) group by messageid"
        cursor.execute(query, (groupname, usrid,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def insertGroup(self, name, userid):
        cursor = self.connection.cursor()
        query = "with insert1 as (insert into groupchats(groupname, admind, date_created) VALUES (%s, %s, now()) returning admind as usrid, groupid) " \
                "insert into members (usrid, groupid) select usrid, groupid from insert1 returning *;"
        cursor.execute(query, (name, userid))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    def insertMember(self, gid, item):
        cursor = self.connection.cursor()
        query = "insert into members (usrid, groupid) VALUES" \
                " ((select usrid from users where uphone=%s or uusername =%s), (select groupid from groupchats " \
                "where groupname=%s)) returning *;"
        cursor.execute(query, (item, item, gid,))
        result = cursor.fetchone()
        self.connection.commit()
        return result
