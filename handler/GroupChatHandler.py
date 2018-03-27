from dao.GroupChatDAO import GroupChatDAO
from flask import *


class GroupChatHandler:


    def mapAllToDict(self, row):
        groups = []
        groups['group_id'] = row[0]
        groups['group_name'] = row[1]
        groups['group_admin'] = row[2]
        groups['date_created'] = row[3]
        return groups

    def mapIDToDict(self, row):
        gid = []
        gid['group_id'] = row[0]
        return gid

    def mapNameToDict(self, row):
        name = []
        name['group_name'] = row[0]
        return name

    def mapAdminToDict(self, row):
        admin = []
        admin['group_admin'] = row[0]
        return admin

    def mapDateToDict(self, row):
        date = []
        date['date_created'] = row[0]
        return date

    def getGroups(self):
        dao = GroupChatDAO()
        result = dao.getGroups()
        groups = []
        for i in result:
            groups.append(self.mapAllToDict(i))
        return jsonify(Groups=groups)

    def getGroupByName(self, name):
        dao = GroupChatDAO()
        result = dao.getGroupByName(name)
        mapped = []
        if result is None:
            return jsonify(ERROR='No group found by that name')
        for r in result:
            mapped.append(self.mapAllToDict(r))
        return jsonify(Groups=mapped)

    def getGroupByID(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupByID(gid)
        mapped = []
        if result is None:
            return jsonify(ERROR='No group found with that ID')
        for r in result:
            mapped.append(self.mapAllToDict(r))
        return jsonify(Groups=mapped)

    def getGroupID(self, name):
        dao = GroupChatDAO()
        result = dao.getGroupID(name)
        mapped = []
        if result is None:
            return jsonify(ERROR='No group found by that name')
        for r in result:
            mapped.append(self.mapNameToDict(r[0]), self.mapIDToDict(r[1]))
        return jsonify(Groups=mapped)

    def getGroupNames(self):
        dao = GroupChatDAO()
        result = dao.getGroupNames()
        mapped = []
        if result is None:
            return jsonify(ERROR='No group found')
        for r in result:
            mapped.append(self.mapNameToDict(r))
        return jsonify(Groups=mapped)

    def getGroupAdmin(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupAdmin(gid)
        if result is None:
            return jsonify(ERROR='No group found with that ID')
        for r in result:
            mapped.append(self.mapNameToDict(r[0]), self.mapAdminToDict(r[1]))
        return jsonify(Groups=mapped)

    def getGroupDate(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupDate(gid)
        if result is None:
            return jsonify(ERROR='No group found with that ID')
        for r in result:
            mapped.append(self.mapNameToDict(r[0]), self.mapDateToDict(r[1]))
        return jsonify(Groups=mapped)
