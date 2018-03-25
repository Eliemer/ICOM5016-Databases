from flask import *
from dao.MessagesDAO import *


class MessagesHandler:
    def sort(self, row):
        messages = {}
        messages['id'] = row[0]
        messages['name'] = row[1]
        messages['message'] = row[2]
        return messages

    def getMessages(self):
        dao = MessagesDAO()
        result = dao.getMessages()
        message=[]
        for i in result:
            message.append(self.sort(i))
        return jsonify(Messages=message)

    def getUserMessagesById(self, usrid):
        dao = MessagesDAO()
        result = dao.getUserMessagebyId(usrid)
        message = []
        if result is None:
            return jsonify(Error='Id not in Database')
        for i in result:
            message.append(self.sort(i))
        return jsonify(Message=message)
