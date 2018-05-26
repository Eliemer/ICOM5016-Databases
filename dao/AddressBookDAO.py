from config.db_config import pg_config, dbconnect
import psycopg2
import os


class AddressBookDAO:
    def __init__(self):
        # Uncomment for heroku use
        # DATABASE_URL = os.environ['HEROKU_POSTGRESQL_PINK_URL']
        #
        # self.connection = psycopg2._connect(DATABASE_URL)

        # Uncomment for local use
        connUrl = dbconnect
        self.connection = psycopg2._connect(connUrl)

    def getContactLists(self):
        cursor = self.connection.cursor()
        query = "select * from contactlist;"
        cursor.execute(query)
        result = []
        for contact in cursor:
            result.append(contact)
        return result

    def getContactListbyUser(self, usrid):
        cursor = self.connection.cursor()
        query = "select * from contactlist where usrid = %s;"
        cursor.execute(query, (usrid,))
        users = []
        for u in cursor:
            users.append(u)
        return users

    def getUserContacts(self, usrid):
        cursor = self.connection.cursor()
        query = "select * from contactlist inner join users u on " \
                "contactlist.contactid = u.usrid where contactlist.usrid=%s order by u.ulastname;"
        cursor.execute(query, (usrid, ))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def addContact(self, userid, item):
        cursor = self.connection.cursor()
        query = "insert into contactlist (usrid, contactid) VALUES " \
                "(%s, (select usrid from users where uphone=%s or email=%s)) returning *;"
        cursor.execute(query, (userid, item, item,))
        result = cursor.fetchone()
        self.connection.commit()
        return result
