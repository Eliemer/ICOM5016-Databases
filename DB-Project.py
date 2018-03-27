from flask import Flask
from handler.UserHandler import *
from handler.MessagesHandler import *
from handler.GroupChatHandler import *

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page of Whatsapp Fatulo'


@app.route('/login')
def login():
    return "Thanks for login in"


@app.route('/Users')
def getUsers():
    user = UserHandler()
    return user.getUsers()


@app.route('/Users/Profile/<name>')
def getUsersByName(name):
    return UserHandler().getUsersByName(name)


@app.route('/Users/<int:usrid>')
def getUserById(usrid):
    return UserHandler().getUserById(usrid)


@app.route('/Users/Email')
def getUsersMessages():
    return UserHandler().getUsersEmails()


@app.route('/Messages')
def getMessages():
    return MessagesHandler().getMessages()


@app.route('/Messages/UserMessages/<int:usrid>')
def getUserMessagesById(usrid):
    return MessagesHandler().getUserMessagesById(usrid)


@app.route('/Groupchats')
def getGroupChats():
    return GroupChatHandler().getGroups()


@app.route('/Groupchats/<int:gid>')
def getGrouChatsById(gid):
    return GroupChatHandler().getGroupByID(gid)


@app.route('/Groupchats/Admin/<int:admin>')
def getGroupAdmin(admin):
    return GroupChatHandler().getGroupAdmin(admin)


if __name__ == '__main__':
    app.run()
