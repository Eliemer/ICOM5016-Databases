from config.db_config import pg_config
import psycopg2
import os


class AddressBookDAO:
    def __init__(self):
        # Uncomment for heroku use
        DATABASE_URL = os.environ['DATABASE_URL']

        self.connection = psycopg2._connect(DATABASE_URL)

        # Uncomment for local use
        # connUrl = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        #                                              pg_config['user'],
        #                                              pg_config['password'])
        # self.connection = psycopg2._connect(connUrl)

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
                "contactlist.contactid = u.usrid where contactlist.usrid=%s;"
        cursor.execute(query, (usrid, ))
        result = []
        for r in cursor:
            result.append(r)
        return result
