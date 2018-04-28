from dao.AddressBookDAO import  AddressBookDAO
from flask import *

class AddressBook:
    def arrangeAddressBook(self, row):
        address = {}
        address['name'] = row[2]
        address['phone'] = row[3]
        address['email'] = row[4]
        return address

    def arrangeContacts(self, row):
        contacts = {}
        contacts['Contact ID'] = row[2]
        contacts['Name'] = row[3] + " " + row[4]
        contacts['Phone'] = row[5]
        contacts['Email'] = row[6]
        return contacts

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
            contacts.append(self.arrangeAddressBook(r))
        if contacts:
            return jsonify(Contacts=contacts)
        return jsonify(ERROR='No contact list found')

    def getUserContacts(self, usrid):
        dao = AddressBookDAO()
        result = dao.getUserContacts(usrid)
        contacts = []
        if result:
            for r in result:
                contacts.append(self.arrangeContacts(r))
            return jsonify(Contacts=contacts)
        return jsonify(ERROR='No Contact List for the User')

