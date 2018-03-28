from dao.GroupChatDAO import GroupChatDAO
from flask import *


class GroupChatHandler:

    def arrange(self, row):
        groups = {}
        groups['group_id'] = row[0]
        groups['group_name'] = row[1]
        groups['group_admin'] = row[2]
        groups['date_created'] = row[3]
        return groups

    def arrangeGroupID(self, row):
        groups = {}
        groups['group_id'] = row[0]
        return groups

    def arrangeGroupName(self, row):
        groups = {}
        groups['group_name'] = row[1]
        return groups

    def arrangeGroupAdmin(self, row):
        groups = {}
        groups['group_admin'] = row[2]
        return groups

    def arrangeDateCreated(self, row):
        groups = {}
        groups['date_created'] = row[3]
        return groups

    def getGroups(self):
        dao = GroupChatDAO()
        result = dao.getGroups()
        groups = []
        for i in result:
            groups.append(self.arrange(i))
        return jsonify(Groups=groups)

    def getGroupByName(self, name):
        dao = GroupChatDAO()
        result = dao.getGroupByName(name)
        if result is None:
            return jsonify(ERROR='No group found by that name')
        return jsonify(Groups=result)

    def getGroupByID(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupByID(gid)
        if result is None:
            return jsonify(ERROR='No group found with that ID')
        return jsonify(Group=result)

    def getGroupAdmin(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupAdmin(gid)
        if result is None:
            return jsonify(ERROR='No group found with that ID')
        return jsonify(Group=result)

    def getGroupNames(self):
        dao = GroupChatDAO()
        result = dao.getGroupNames()
        if result is None:
            return jsonify(ERROR='No group found')
        return jsonify(Group=result)
