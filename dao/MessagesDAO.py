from config.db_config import pg_config, dbconnect
import psycopg2
import os


class MessagesDAO:
    def __init__(self):
        # Uncomment for heroku use
        # DATABASE_URL = os.environ['HEROKU_POSTGRESQL_PINK_URL']
        #
        # self.connection = psycopg2._connect(DATABASE_URL)

        # Uncomment for local use
        connUrl = dbconnect
        self.connection = psycopg2._connect(connUrl)

    def getMessages(self):
        cursor = self.connection.cursor()
        query = "select * from messages;"
        cursor.execute(query)
        result = []
        for mess in cursor:
            result.append(mess)
        return result

    def getUserMessagebyId(self, usrid):
        cursor = self.connection.cursor()
        query = "select ufirstname, ulastname, content from Users natural inner join Messages where messages.usrid = %s;"
        cursor.execute(query, (usrid,))
        result = []
        for m in cursor:
            result.append(m)
        return result

    def getMessageLikes(self,name, mid):
        cursor = self.connection.cursor()
        query = "select * from users natural inner join likes natural inner join members " \
                "natural inner join groupchats where messageid=%s and groupname=%s;"
        cursor.execute(query, (mid, name, ))
        result = []
        for m in cursor:
            result.append(m)
        return result

    def getMessageDislikes(self, gid, mid):
        cursor = self.connection.cursor()
        query = "select * from users natural inner join dislike natural inner join members " \
                    "natural inner join groupchats where messageid=%s and groupname=%s;"
        cursor.execute(query, (mid, gid))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getMessageReplies(self, gid, mid):
        cursor = self.connection.cursor()
        query = "select * from users inner join replies using(usrid) inner join members using(usrid)" \
                " inner join groupchats using(groupid) where messageid=%s and groupname=%s;"
        cursor.execute(query, (mid, gid, ))
        result = []
        for r in cursor:
            result.append(r)
        return result


    def getNumberOfLikes(self, mid):
        cursor = self.connection.cursor()
        query = "select count(*) from likes where messageid=%s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getNumberOfDislikes(self, mid):
        cursor = self.connection.cursor()
        query = "select count(*) from dislike where messageid=%s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getReactions(self, mid):
        cursor = self.connection.cursor()
        query = "select count(*) as l, count(*) as dl from likes inner join dislike using(messageid) where messageid=%s;"
        cursor.execute(query, (mid, ))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getHashtags(self):
        result = []
        for m in self.messages:
            h = m[4].split('#')
            if len(h) > 1:
                result.append('#' + h[1])
        return result

    def insertMessage(self, group, userid, message):
        cursor = self.connection.cursor()
        query = "insert into messages (groupid, usrid, date_sent, content) VALUES " \
                "((select groupid from groupchats where groupname=%s), %s, now(), %s) returning *;"
        cursor.execute(query, (group, userid, message,))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    def insertLike(self, mid, user):
        cursor = self.connection.cursor()
        query = "insert into likes (messageid, usrid) VALUES (%s, %s) on conflict do nothing returning *;"
        cursor.execute(query, (mid, user,))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    def insertDislike(self, mid, user):
        cursor = self.connection.cursor()
        query = "insert into dislike (messageid, usrid) VALUES (%s, %s) on conflict do nothing returning *;"
        cursor.execute(query, (mid, user,))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    def insertReply(self, mid, user, groupname, content):
        cursor = self.connection.cursor()
        query = "with old_msg as (select * from messages where messageid=%s), " \
                "new_mess as (insert into messages (groupid, usrid, date_sent, content) " \
                "VALUES ((select groupid from groupchats where groupname= %s), %s, now(), " \
                "concat(concat(concat('\"RE: ',(select old_msg.content from old_msg)), '\" '), %s)) " \
                "returning messageid, usrid, content) insert into  replies (messageid, usrid, reply_message) " \
                "values (%s,(select usrid from new_mess),(select content from new_mess))  returning *;"
        cursor.execute(query, (mid, groupname, user, content, mid))
        result = cursor.fetchone()
        self.connection.commit()
        return result
