from flask import Flask, jsonify, request
from handler.UserHandler import *
from handler.MessagesHandler import *
from handler.GroupChatHandler import *
from handler.AddressBook import *
from flask_cors import cross_origin, CORS

app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/JEChat/login')
def login():
    return "Thanks for login in"


# <------------------ Routes for User fetching actions
@app.route('/JEChat/Users')
def getUsers():
    users = UserHandler().getUsers()
    return users


@app.route('/JEChat/<username>')
def getUsersByName(username):
    return UserHandler().getUsersByUsername(username)


@app.route('/JEChat/<int:usrid>')
def getUserById(usrid):
    return UserHandler().getUserById(usrid)


@app.route('/JEChat/Users/Emails')
def getUsersMessages():
    return UserHandler().getUsersEmails()


@app.route('/JEChat/Users/<username>')
def getUsersByUsername(username):
    return UserHandler().getUserByName(username)
# End of User actions ------------------------------------------->


# Routes for Messages fetching actions
@app.route('/JEChat/Messages')
def getMessages():
    return MessagesHandler().getMessages()


@app.route('/JEChat/Users/<int:id>/Messages')
def getUserMessagesById(usrid):
    return MessagesHandler().getUserMessagesById(usrid)


@app.route('/JEChat/<name>/Messages/<int:mid>/likes')
def getMessageLikes(name, mid):
    return MessagesHandler().getMessageLikes(name, mid)


@app.route('/JEChat/<gid>/Messages/<int:mid>/dislikes')
def getMessageDislikes(gid, mid):
    return MessagesHandler().getMessageDislikes(gid, mid)


@app.route('/JEChat/<gid>/Messages/<int:mid>/replies')
def getMessageReplies(gid, mid):
    return MessagesHandler().getMessageReplies(gid, mid)


@app.route('/JEChat/Messages/<int:mid>/numberoflikes')
def getNumberOfLikes(mid):
    return MessagesHandler().getNumberOfLikes(mid)

@app.route('/JEChat/Messages/<int:mid>/numberofdislikes')
def getNumberOfDislikes(mid):
    return MessagesHandler().getNumberOfDislikes(mid)


@app.route('/JEChat/Messages/<int:mid>/likes&dislikes')
def getReactions(mid):
    return MessagesHandler().getReactions(mid)
# End of Messages actions -------------------------------------->


# <---------------------------Routes for GroupChats fetching actions
@app.route('/JEChat/GroupChats')
def getGroupChats():
    return GroupChatHandler().getAllGroups()

@app.route('/JEChat/GroupChats/<name>')
def getGroupchatContent(name):
    return GroupChatHandler().getGroupContent(name)


@app.route('/JEChat/GroupChats/<int:gid>')
def getGrouChatsById(gid):
    return GroupChatHandler().getGroupByID(gid)


@app.route('/JEChat/GroupChats/<int:gid>/Members')
def getUsersInGroup(gid):
    return GroupChatHandler().getUsersInGroup(gid)


@app.route('/JEChat/GroupChats/<int:gid>/Admin')
def getGroupAdmin(gid):
    return GroupChatHandler().getGroupAdmin(gid)


@app.route('/JEChat/GroupChats/Names')
def getGroupNames():
    return GroupChatHandler().getAllGroupNames()


@app.route('/JEChat/<int:usrid>/GroupChats')
def getUserGroupchats(usrid):
    return GroupChatHandler().getUserGroupchats(usrid)


@app.route('/JEChat/<int:usrid>/GroupChats/<groupname>')
def getUserGroupContent(usrid, groupname):
    return GroupChatHandler().getUserGroupContent(usrid, groupname)


@app.route('/JEChat/<int:usrid>/GroupChats/<groupname>/reactionlikes')
def getUserGroupReactions(usrid, groupname):
    return GroupChatHandler().getUGMLikes(usrid, groupname)
# End fo GroupChat fetching actions --------------------------->


# <---------------- Routes for Contact Lists actions
@app.route('/JEChat/ContactLists')
def getContactLists():
    return AddressBook().getContactLists()


@app.route('/JEChat/<int:usrid>/ContactList')
def getContactsByUser(usrid):
    return AddressBook().getUserContacts(usrid)


# End of Contact List actions ------------------->
# <----------------------Routes for Hashtags actions

@app.route('/JEChat/TrendingHashtags')
def getHashtags():
    return MessagesHandler().getHashtags()


if __name__ == '__main__':
    app.run(port=4545)
