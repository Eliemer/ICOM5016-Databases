class GroupChatDAO:

    def __init__(self):
        self.groups = []
        G1 = [1982, 'Wannabes', 158, '03-04-2017']
        G2 = [870, 'ININ4010', 584, '02-17-2018']
        G3 = [137, 'Friend\'s Club', 265, '08-27-2015']
        G4 = [1087, 'ICOM 5016 - Databases', 265, '02-14-2018']
        G5 = [497, 'Pedrito\'s personal hell', 584, '08-29-2017']
        G6 = [798, 'Batman\'s Fanclub', 965, '07-11-2013']
        self.groups.append(G1)
        self.groups.append(G2)
        self.groups.append(G3)
        self.groups.append(G4)
        self.groups.append(G5)
        self.groups.append(G6)

    def getGroups(self):
        return self.groups

    def getGroupByName(self, name):
        groups = []
        for g in self.groups:
            if name == g[1]:
                groups.append(g)
        return groups

    def getGroupByID(self, gid):
        group = []
        for g in self.groups:
            if gid == g[0]:
                group.append(g)
        return group

    def getGroupID(self, name):
        group = []
        for g in self.groups:
            if name == g[1]:
                group.append(g)
        return group

    def getGroupName(self, gid):
        group = []
        for g in self.groups:
            if gid == g[0]:
                group.append(g)
        return group

    def getGroupAdmin(self, gid):
        admin = []
        for g in self.groups:
            if gid == g[0]:
                admin.append(g)
        return admin

    def getGroupDate(self, gid):
        date = []
        for g in self.groups:
            if gid == g[0]:
                date.append(g)
        return date


