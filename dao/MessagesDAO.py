from config.db_config import pg_config
import psycopg2


class MessagesDAO:
    def __init__(self):
        connUrl = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                     pg_config['user'],
                                                     pg_config['password'])
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

    def getHashtags(self):
        result = []
        for m in self.messages:
            h = m[4].split('#')
            if len(h) > 1:
                result.append('#' + h[1])

        return result
