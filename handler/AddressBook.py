from dao.AddressBookDAO import  AddressBookDAO
from flask import *

class AddressBook:
    def arrangeAddressBook(self, row):
        address = {}
        address['usrid'] = row[0]
        address['name'] = row[1]
        address['phone'] = row[2]
        address['email'] = row[3]
        return address

    def arrangeContactList(self, row):
        contact = {}
        contact['usrid'] = row[0]
        contact['addressbook_id'] = row[1]
        contact['addressbook'] = row[2]
        return contact

    def getContactLists(self):
        dao = AddressBookDAO()
        result = dao.getContactLists()
        contact = []
        for r in result:
            contact.append(self.arrangeContactList(r))
        if contact is not None:
            return jsonify(ContactList=contact)
        else:
            return jsonify(ERROR='No contact list found')

    def getContactListbyUser(self, usrid):
        dao = AddressBookDAO()
        result = dao.getContactListbyUser(usrid)
        contacts = []
        for r in result:
            contacts.append(self.arrangeContactList(r))
        if contacts is not None:
            return jsonify(ContactList=contacts)
        else:
            return jsonify(ERROR='No contact list found')

