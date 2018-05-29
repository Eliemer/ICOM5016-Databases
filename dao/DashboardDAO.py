from config.db_config import pg_config, dbconnect
import psycopg2
import os

class DashboardDAO:
    def __init__(self):
        # Uncomment for heroku use
        # DATABASE_URL = os.environ['HEROKU_POSTGRESQL_PINK_URL']
        #
        # self.connection = psycopg2._connect(DATABASE_URL)

        # Uncomment for local use
        connUrl = dbconnect
        self.connection = psycopg2._connect(connUrl)

    def MessagesPerDay(self):
            cursor = self.connection.cursor()
            query = "select count(*), to_char(date_sent, 'MM-DD') as day  from messages group by day order by day;"
            cursor.execute(query)
            result = []
            for r in cursor:
                result.append(r)
            return result

    def LikesPerDay(self):
        cursor = self.connection.cursor()
        query = "select count(*), to_char(me.date_sent, 'MM-DD') as day " \
                "from messages as me inner join likes l on me.messageid = l.messageid group by day order by day desc;"
        cursor.execute(query)
        result = []
        for r in cursor:
            result.append(r)
        return result

    def DislikesPerDay(self):
        cursor = self.connection.cursor()
        query = "select count(*), to_char(me.date_sent, 'MM-DD') as day " \
                "from messages as me inner join dislike d on me.messageid = d.messageid group by day order by day desc;"
        cursor.execute(query)
        result = []
        for r in cursor:
            result.append(r)
        return result

    def RepliesPerDay(self):
        cursor = self.connection.cursor()
        query = "select count(*), to_char(r.date_sent, 'MM-DD') as day " \
                "from messages inner join replies r on messages.messageid = r.messageid group by day order by day desc;"
        cursor.execute(query)
        result = []
        for r in cursor:
            result.append(r)
        return result

    def TrendingHashtags(self):
        cursor = self.connection.cursor()
        query = "select hashtag, count(*) from hashtags group by hashtag order by count(*) desc fetch first 10 rows only;"
        cursor.execute(query)
        result = []
        for r in cursor:
            result.append(r)
        return result

    def ActiveUsers(self):
        cursor = self.connection.cursor()
        query = "select count(*) as count, to_char(me.date_sent, 'MM-DD') as day, usrid " \
                "from messages as me natural inner join users group by day, usrid order by day desc, count desc;"
        cursor.execute(query)
        result = []
        for r in cursor:
            result.append(r)
        return result