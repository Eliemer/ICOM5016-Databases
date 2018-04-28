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


@app.route('/ConvWorld/login')
def login():
    return "Thanks for login in"


# <------------------ Routes for User fetching actions
@app.route('/ConvWorld/Users')
def getUsers():
    users = UserHandler().getUsers()
    return users


@app.route('/ConvWorld/<username>')
def getUsersByName(username):
    return UserHandler().getUsersByUsername(username)


@app.route('/ConvWorld/<int:usrid>')
def getUserById(usrid):
    return UserHandler().getUserById(usrid)


@app.route('/ConvWorld/Users/Emails')
def getUsersMessages():
    return UserHandler().getUsersEmails()


@app.route('/ConvWorld/Users/<username>')
def getUsersByUsername(username):
    return UserHandler().getUserByName(username)
# End of User actions ------------------------------------------->


# Routes for Messages fetching actions
@app.route('/ConvWorld/Messages')
def getMessages():
    return MessagesHandler().getMessages()


@app.route('/ConvWorld/Users/<int:id>/Messages')
def getUserMessagesById(usrid):
    return MessagesHandler().getUserMessagesById(usrid)


@app.route('/ConvWorld/<name>/Messages/<int:mid>/likes')
def getMessageLikes(name, mid):
    return MessagesHandler().getMessageLikes(name, mid)


@app.route('/ConvWorld/<gid>/Messages/<int:mid>/dislikes')
def getMessageDislikes(gid, mid):
    return MessagesHandler().getMessageDislikes(gid, mid)


@app.route('/ConvWorld/<gid>/Messages/<int:mid>/replies')
def getMessageReplies(gid, mid):
    return MessagesHandler().getMessageReplies(gid, mid)


@app.route('/ConvWorld/Messages/<int:mid>/numberoflikes')
def getNumberOfLikes(mid):
    return MessagesHandler().getNumberOfLikes(mid)

@app.route('/ConvWorld/Messages/<int:mid>/numberofdislikes')
def getNumberOfDislikes(mid):
    return MessagesHandler().getNumberOfDislikes(mid)


@app.route('/JEChat/Messages/<int:mid>/likes&dislikes')
def getReactions(mid):
    return MessagesHandler().getReactions(mid)
# End of Messages actions -------------------------------------->


# <---------------------------Routes for GroupChats fetching actions
@app.route('/ConvWorld/GroupChats')
def getGroupChats():
    return GroupChatHandler().getAllGroups()

@app.route('/ConvWorld/GroupChats/<name>/')
def getGroupchatContent(name):
    return GroupChatHandler().getGroupContent(name)


@app.route('/ConvWorld/GroupChats/<int:gid>')
def getGrouChatsById(gid):
    return GroupChatHandler().getGroupByID(gid)


@app.route('/ConvWorld/GroupChats/<int:gid>/Members')
def getUsersInGroup(gid):
    return GroupChatHandler().getUsersInGroup(gid)


@app.route('/ConvWorld/GroupChats/Admin/<int:admin>')
def getGroupAdmin(admin):
    return GroupChatHandler().getGroupAdmin(admin)


@app.route('/ConvWorld/GroupChats/Names')
def getGroupNames():
    return GroupChatHandler().getAllGroupNames()


@app.route('/ConvWorld/<int:usrid>/GroupChats')
def getUserGroupchats(usrid):
    return GroupChatHandler().getUserGroupchats(usrid)


# End fo GroupChat fetching actions --------------------------->


# <---------------- Routes for Contact Lists actions
@app.route('/ConvWorld/ContactLists')
def getContactLists():
    return AddressBook().getContactLists()


@app.route('/ConvWorld/<int:usrid>/ContactList')
def getContactsByUser(usrid):
    return AddressBook().getUserContacts(usrid)


# End of Contact List actions ------------------->
# <----------------------Routes for Hashtags actions

@app.route('/ConvWorld/TrendingHashtags')
def getHashtags():
    return MessagesHandler().getHashtags()


if __name__ == '__main__':
    app.run(port=4545)
