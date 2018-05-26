from dao.MessagesDAO import MessagesDAO
from config.db_config import pg_config, dbconnect
import psycopg2
import os


class HashtagDAO:
    def __init__(self):
        # Uncomment for heroku use
        # DATABASE_URL = os.environ['HEROKU_POSTGRESQL_PINK_URL']
        #
        # self.connection = psycopg2._connect(DATABASE_URL)

        # Uncomment for local use
        connUrl = dbconnect
        self.connection = psycopg2._connect(connUrl)


    def getHashtags(self):
        cursor = self.connection.cursor()
        query = "select * from hashtags;"
        cursor.execute(query)
        result = []
        for r in cursor:
            result.append(r)
        return result

    def parseHashtag(self, result):
        hash = []
        for r in result['MessageContent'].split():
            if r.startswith('#'):
                hashtags = {'hashtag': r, 'messageid': result['MessageID']}
                text = r
                mid = result['MessageID']
                self.insertHashtag(text, mid)
                hash.append(hashtags)
        return hash

    def insertHashtag(self, text, mid):
        cursor = self.connection.cursor()
        query = "insert into hashtags (hashtag, messageid) VALUES (%s, %s) returning *;"
        cursor.execute(query, (text, mid,))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    def parseHash(self, result):
        hash = []
        for r in result['content'].split():
            if r.startswith('#'):
                hashtags = {'hashtag': r, 'messageid': result['mid']}
                text = r
                mid = result['mid']
                self.insertHashtag(text, mid)
                hash.append(hashtags)
        return hash







