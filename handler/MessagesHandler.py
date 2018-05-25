from flask import *
from dao.MessagesDAO import *
from dao.HashtagDAO import *


class MessagesHandler:
    def arrange(self, row):
        messages = {}
        messages['MessageID'] = row[0]
        messages['GroupID'] = row[1]
        messages['UserID'] = row[2]
        messages['Datesent'] = row[3]
        messages['MessageContent'] = row[4]
        return messages

    def arrangeJoin(self, row):
        messages = {}
        messages['First Name'] = row[0]
        messages['Last Name'] = row[1]
        messages['Text'] = row[2]
        return messages

    def arrangebeta(self, row):
        contents={}
        #contents['Group ID'] = row[0]
        #contents['User ID'] = row[1]
        contents['firstname'] = row[2]
        contents['lastname'] = row[3]
        contents['phone'] = row[4]
        contents['email'] = row[5]
        #contents['Username'] = row[6]
        #contents['Message ID'] = row[8]
        contents['likes'] = row[9]
        contents['groupname'] = row[10]
        #contents['Date Created'] = row[12]
        return contents

    def arrangelike(self, row):
        likes = {}
        likes['#ofLikes'] = row[0]
        return likes

    def arrangedislike(self, row):
        likes = {}
        likes['#ofDislikes'] = row[0]
        return likes

    def arrangelikesbeta(self, row):
        contents={}
        contents['Message'] = row[0]
        contents['likes'] = row[1]
        contents['dislikes'] = row[2]
        return contents

    def arrangereactions(self, row):
        reactions = {}
        reactions['Likes'] = row[0][0]
        reactions['Dislikes'] = row[0][1]
        return reactions

    def arrangeLikes(self, row):
        likes = {'messageid': row[0], 'usrid': row[1]}
        return likes

    def arrangeEcho(self, row):
        return {'messageid': row[0], 'usrid': row[1]}


    # def arrangeMessageID(self, row):
    #     message = {}
    #     message['message_id'] = row[0]
    #     return message
    #
    # def arrangeMessageSenderID(self, row):
    #     message = {}
    #     message['sender_id'] = row[1]
    #     return message
    #
    # def arrangeMessageGroupID(self, row):
    #     message = {}
    #     message['group_id'] = row[2]
    #     return message
    #
    # def arrangeMessageDateSent(self, row):
    #     message = {}
    #     message['date_sent'] = row[3]
    #     return message
    #
    # def arrangeMessageSenderID(self, row):
    #     message = {}
    #     message['message_content'] = row[4]
    #     return message

    def getMessages(self):
        dao = MessagesDAO()
        result = dao.getMessages()
        message = []
        for i in result:
            message.append(self.arrange(i))
        return jsonify(Messages=message)

    def getUserMessagesById(self, usrid):
        dao = MessagesDAO()
        result = dao.getUserMessagebyId(usrid)
        message = []
        if result:
            for m in result:
                message.append(self.arrangeJoin(m))
            return jsonify(Messages=message)
        return jsonify(ERROR='No messages from that User')

    def getMessageLikes(self,name, mid):
        dao = MessagesDAO()
        result = dao.getMessageLikes(name, mid)
        res = []
        if result:
            for r in result:
                res.append(self.arrangebeta(r))
            return jsonify(Message=res)
        return jsonify(ERROR='No one has liked this message')

    def getMessageDislikes(self, gid, mid):
        dao = MessagesDAO()
        result = dao.getMessageDislikes(gid, mid)
        res = []
        if result:
            for r in result:
                res.append(self.arrangebeta(r))
            return jsonify(Message=res)
        return jsonify(ERROR='No one has disliked this message')

    def getMessageReplies(self, gid, mid):
        dao = MessagesDAO()
        result = dao.getMessageReplies(gid, mid)
        res = []
        if result:
            for r in result:
                res.append(self.arrangebeta(r))
            return jsonify(Replies=res)
        return jsonify(ERROR='No replies for that message')

    def getNumberOfLikes(self, mid):
        dao = MessagesDAO()
        result = dao.getNumberOfLikes(mid)
        if result:
            res = self.arrangelike(result)
            return jsonify(Message_Likes=res)
        return jsonify(ERROR='0 Likes')

    def getNumberOfDislikes(self, mid):
        dao = MessagesDAO()
        result = dao.getNumberOfDislikes(mid)
        if result:
            res = self.arrangedislike(result)
            return jsonify(Message_Disikes=res)
        return jsonify(ERROR='0 Likes')

    def getReactions(self, mid):
        dao = MessagesDAO()
        result = dao.getReactions(mid)
        if result:
            res = self.arrangereactions(result)
            return jsonify(Reactions=res)
        return jsonify(ERROR='0 Reactions')


    def getHashtags(self):
        dao = MessagesDAO()
        result = dao.getHashtags()
        return jsonify(Hashtags=result)

    def insertMessage(self, form, userid, groupname):
        if len(form) != 1:
            return jsonify(ERROR='Malformed request form')
        else:
            group = groupname
            usrid = userid
            content = form['content']
            if group and usrid and content:
                dao = MessagesDAO()
                mess = dao.insertMessage(group, usrid, content)
                if mess:
                    result = self.arrange(mess)
                    hashtag = HashtagDAO().parseHashtag(result)
                    return jsonify(Message={'Message': result, 'Hashtags': hashtag})
                else:
                    return jsonify(ERROR='Could not post message')
            else:
                return jsonify(ERROR='Wrong form posted')

    def insertLikes(self, form):
        if len(form) != 2:
            return jsonify(ERROR='Malformed request form')
        else:
            mid = form['mid']
            user = form['user']
            if mid and user:
                dao = MessagesDAO()
                mess = dao.insertLike(mid, user)
                if mess:
                    result = self.arrangeLikes(mess)
                    return jsonify(Likes=result)
                else:
                    return jsonify(ERROR='Could not post like')

    def insertDislikes(self, form):
        if len(form) != 2:
            return jsonify(ERROR='Malformed request form')
        else:
            mid = form['mid']
            user = form['user']
            if mid and user:
                dao = MessagesDAO()
                mess = dao.insertDislike(mid, user)
                if mess:
                    result = self.arrangeEcho(mess)
                    return jsonify(Dislikes=result)
                else:
                    return jsonify(ERROR='Could not post like')

    def insertReply(self, form):
        if len(form) != 4:
            return jsonify(ERROR='Malformed request form')
        else:
            mid = form['mid']
            user = form['user']
            groupname = form['groupname']
            content = form['content']
            res = {'content': content, 'mid': mid};
            if mid and user and groupname and content:
                dao = MessagesDAO()
                mess = dao.insertReply(mid, user, groupname, content)
                if mess:
                    result = self.arrangeEcho(mess)
                    hashtag = HashtagDAO().parseHash(res)
                    return jsonify(Reply=result)
                else:
                    return jsonify(ERROR='Could not post like')


