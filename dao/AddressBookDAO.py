from dao.UserDAO import *


class AddressBookDAO:
    def __init__(self):
        self.address1 = []
        # p = [id, name, phone, email]
        p1 = [652, 'Pablo ICOM', '7879654859', 'blank']
        p2 = [654, 'Juan Termo', '7874256598', 'loki@asgard.com']
        p3 = [26, 'Pedro Diablo', '9396526859', 'thor@asgard.com']
        p4 = [56, 'Mami', '9396254865', 'blank']
        self.address1.append(p1)
        self.address1.append(p2)
        self.address1.append(p3)
        self.address1.append(p4)

        self.address2 = []
        # q = [id, name, phone, email]
        q1 = [154, 'Liz BIOL', '9396521452','example@example.com']
        q2 = [584, 'Lucas INME', '7879521265', 'notexample@notexample.com']
        q3 = [256, 'Mami', '7874526584', 'mom@parent.com']
        q4 = [632,'Papi', '7872514845', 'dad@parent.com']
        self.address2.append(q1)
        self.address2.append(q2)
        self.address2.append(q3)
        self.address2.append(q4)

        self.contactList = []
        # A = [user id, addressbook id, address
        A1 = [UsersDAO().users[0][0], 346, self.address1]
        A2 = [UsersDAO().users[1][0], 456, self.address2]
        self.contactList.append(A1)
        self.contactList.append(A2)

    def getContactLists(self):
        return self.contactList

    def getContactListbyUser(self, usrid):
        users = []
        for u in self.contactList:
            if usrid == u[0]:
                users.append(u)
        return users
