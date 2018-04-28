from dao.GroupChatDAO import GroupChatDAO
from flask import *


class GroupChatHandler:

    def arrange(self, row):
        groups = {}
        groups['GroupChat id'] = row[0]
        groups['GroupChat Name'] = row[1]
        groups['GroupChat Admin'] = row[2]
        groups['Date Created'] = row[3]
        return groups

    def arrangeAlpha(self, row):
        groups = {}
        groups['GroupChat id'] = row[0]
        groups['GroupChat Name'] = row[1]
        groups['Admin'] = row[2] + " " + row[3]
        groups['Date Created'] = row[4]
        return groups

    def arrangeBeta(self, row):
        groups = {}
        groups['GroupChat Name'] = row[1]
        groups['Date Created'] = row[3]
        return groups

    def arrangeGroupID(self, row):
        groups = {}
        groups['group_id'] = row[0]
        return groups

    def arrangeGroupName(self, row):
        groups = {}
        groups['group_name'] = row[0]
        return groups

    def arrangeGroupAdmin(self, row):
        groups = {}
        groups['group_admin'] = row[2]
        return groups

    def arrangeDateCreated(self, row):
        groups = {}
        groups['date_created'] = row[3]
        return groups

    def arrangeContent(self, row):
        content = {}
        content['Name'] = row[0] + " " + row[1]
        content['Content'] = row[2]
        content['Sent in:'] = row[3]
        return content

    def arrangeMembers(self, row):
        members = {}
        members['Name'] = row[0] + " " + row[1]
        return members

    def getAllGroups(self):
        dao = GroupChatDAO()
        result = dao.getGroups()
        groups = []
        if result:
            for i in result:
                groups.append(self.arrangeAlpha(i))
            return jsonify(Groups=groups)
        return jsonify(ERROR='No groups found')

    def getAllGroupIDs(self):
        dao = GroupChatDAO()
        result = dao.getGroups()
        groups = []
        if result is None:
            return jsonify(ERROR='No groups found')
        for i in result:
            groups.append(self.arrangeGroupID(i))
        return jsonify(Groups=groups)

    def getAllGroupNames(self):
        dao = GroupChatDAO()
        result = dao.getGroupNames()
        group = []
        if result is None:
            return jsonify(ERROR='No groups found')
        for i in result:
            group.append(self.arrangeGroupName(i))
        return jsonify(Group=result)

    def getAllGroupAdmins(self):
        dao = GroupChatDAO()
        result = dao.getGroupNames()
        group = []
        if result is None:
            return jsonify(ERROR='No groups found')
        for i in result:
            group.append(self.arrangeGroupAdmin(i))
        return jsonify(Group=result)

    def getAllGroupDateCreated(self):
        dao = GroupChatDAO()
        result = dao.getGroups()
        group = []
        if result is None:
            return jsonify(ERROR='No groups found')
        for i in result:
            group.append(self.arrangeDateCreated(i))
        return jsonify(Group=result)

    def getGroupAdmin(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupAdmin(gid)
        if result is None:
            return jsonify(ERROR='No group found with that ID')
        return jsonify(Group=result)

    def getGroupByName(self, name):
        dao = GroupChatDAO()
        result = dao.getGroupByName(name)
        if result is None:
            return jsonify(ERROR='No group found by that name')
        return jsonify(Groups=result)

    def getGroupByID(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupByID(gid)
        content = []
        if result:
            for r in result:
                content.append(self.arrangeContent(r))
            return jsonify(Content=content)
        return jsonify(ERROR='No GroupChat Found')


    def getGroupContent(self, name):
        dao = GroupChatDAO()
        result = dao.getGroupContent(name)
        content = []
        if result:
            for r in result:
                content.append(self.arrangeContent(r))
            return jsonify(Content=content)
        return jsonify(ERROR='No GroupChat Found')

    def getUsersInGroup(self, gid):
        dao = GroupChatDAO()
        result = dao.getUsersInGroup(gid)
        users = []
        if result:
            for r in result:
                users.append(self.arrangeMembers(r))
            return jsonify(Users_In_GroupChat=users)
        return jsonify(ERROR='That Groupchat doesn''t exists')

    def getUserGroupchats(self, usrid):
        dao = GroupChatDAO()
        result = dao.getUserGroupchats(usrid)
        groupchats = []
        if result:
            for r in result:
                groupchats.append(self.arrangeBeta(r))
            return jsonify(Groupchats=groupchats)
        return jsonify(ERROR="No User found by that ID")


