from flask import *
from dao.MessagesDAO import *


class MessagesHandler:
    def arrange(self, row):
        messages = {}
        messages['Message ID'] = row[0]
        messages['Group ID'] = row[1]
        messages['User ID'] = row[2]
        messages['Date sent'] = row[3]
        messages['Message Content'] = row[4]
        messages['Likes'] = row[5]
        messages['Dislikes'] = row[6]
        return messages

    def arrangeJoin(self, row):
        messages = {}
        messages['First Name'] = row[0]
        messages['Last Name'] = row[1]
        messages['Text'] = row[2]
        return messages

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


    def getHashtags(self):
        dao = MessagesDAO()
        result = dao.getHashtags()
        return jsonify(Hashtags=result)
