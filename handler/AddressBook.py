from dao.AddressBookDAO import  AddressBookDAO
from flask import *

class AddressBook:
    def arrange(self, row):
        address = {}
        address['usrid'] = row[0]
        address['address_id'] = row[1]
        address['addressbook'] = row[2]
        return address

    def getContactLists(self):
        dao = AddressBookDAO()
        result = dao.getContactLists()
        if result:
            return jsonify(ContactList=result)
        else:
            return jsonify(ERROR='No contact list found')

    def getContactListbyUser(self, usrid):
        dao = AddressBookDAO()
        result = dao.getContactListbyUser(usrid)
        if result:
            return jsonify(ContactList=result)
        else:
            return jsonify(ERROR='No contact list found')
