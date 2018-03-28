from flask import *
from dao.MessagesDAO import *


class MessagesHandler:
    def arrange(self, row):
        messages = {}
        messages['message_id'] = row[0]
        messages['sender_id'] = row[1]
        messages['group_id'] = row[2]
        messages['date_sent'] = row[3]
        messages['message_content'] = row[4]
        return messages

    def arrangeMessageID(self, row):
        message = {}
        message['message_id'] = row[0]
        return message

    def arrangeMessageSenderID(self, row):
        message = {}
        message['sender_id'] = row[1]
        return message

    def arrangeMessageGroupID(self, row):
        message = {}
        message['group_id'] = row[2]
        return message

    def arrangeMessageDateSent(self, row):
        message = {}
        message['date_sent'] = row[3]
        return message

    def arrangeMessageSenderID(self, row):
        message = {}
        message['message_content'] = row[4]
        return message

    def getMessages(self):
        dao = MessagesDAO()
        result = dao.getMessages()
        message=[]
        for i in result:
            message.append(self.arrange(i))
        return jsonify(Messages=message)

    def getUserMessagesById(self, usrid):
        dao = MessagesDAO()
        result = dao.getUserMessagebyId(usrid)
        message = []
        if result is None:
            return jsonify(Error='Id not in Database')
        for i in result:
            message.append(self.arrange(i))
        return jsonify(Message=message)

    def getHashtags(self):
        dao = MessagesDAO()
        result = dao.getHashtags()
        return jsonify(Hashtags=result)
