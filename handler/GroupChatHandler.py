from dao.GroupChatDAO import GroupChatDAO
from dao.MessagesDAO import MessagesDAO
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
        groups['groupname'] = row[1]
        groups['date'] = row[3]
        return groups

    def arrangeCharlie(self, row):
        return {
            'messageid': row[0],
            'content': row[1],
            'name': row[2] + ' ' + row[3],
            'likes': row[4],
            'dislikes': row[5]}


    def arrangeDelta(self, row):
        reactions = {}
        reactions['likes'] = row[0]
        reactions['messageid'] = row[1]
        return reactions

    def arrangeGroupID(self, row):
        groups = {}
        groups['usrid'] = row[0]
        groups['groupid'] = row[1]
        return groups

    def arrangeGroupName(self, row):
        groups = {}
        groups['group_name'] = row[0]
        return groups

    def arrangeGroupAdmin(self, row):
        groups = {}
        groups['userid'] = row[0]
        groups['name'] = row[1] + " " + row[2]
        groups['phone'] = row[3]
        groups['email'] = row[4]
        groups['username'] = row[5]
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
        admin = []
        if result:
            for r in result:
                admin.append(self.arrangeGroupAdmin(r))
            return jsonify(Admin=admin)
        return jsonify(ERROR='No Groupchat by that ID')


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

    def getUserGroupContent(self, usrid, groupname):
        dao = GroupChatDAO()
        result = dao.getUserGroupContent(usrid, groupname)
        groupchats = []
        if result:
            for r in result:
                groupchats.append(self.arrangeCharlie(r))
        return jsonify(Groupchats=groupchats)

    def getUGMLikes(self, usrid, groupname):
        dao = GroupChatDAO()
        result = dao.getUGMLikes(usrid, groupname)
        groupchats = []
        if result:
            for r in result:
                groupchats.append(self.arrangeDelta(r))
            return jsonify(Likes=groupchats)
        return jsonify(ERROR="No User found by that ID")

    def insertGroup(self, form, usrid):
        if len(form) != 1:
            return jsonify(ERROR='Malformed request form')
        else:
            name = form['groupname']
            # date = form['date']
            if name and usrid:
                dao = GroupChatDAO()
                group = dao.insertGroup(name, usrid)
                if group:
                    result = self.arrangeGroupID(group)
                    return jsonify(GroupID=result)
                else:
                    return jsonify(ERROR='Creation of groupchat denied')
            else:
                return jsonify(ERROR='Malformed request form')

    def insertMember(self, form):
        if len(form) != 2:
            return jsonify(ERROR='Malformed request form')
        else:
            item = form['credential']  # item can be a phone number o email
            groupname = form['groupname']
            if groupname and item:
                dao = GroupChatDAO()
                result = dao.insertMember(groupname, item)
                if result:
                    return jsonify(Member=self.arrangeGroupID(result))
                else:
                    jsonify(ERROR='User already exists')
            else:
                return jsonify(ERROR='Malformed request form')



