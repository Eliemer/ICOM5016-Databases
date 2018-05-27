from flask_cors import CORS
from flask import Flask, jsonify, request
from handler.AddressBook import *
from handler.GroupChatHandler import *
from handler.MessagesHandler import *
from handler.UserHandler import *
from handler.DashboardHandler import *
from handler.HashtagHandler import *

app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False
CORS(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return render_template('home.html')

# Routes used for deliverables


@app.route('/JEChat/register', methods=['POST'])
def register():
    return UserHandler().insertUser(request.get_json('data '))


@app.route('/JEChat/login', methods=['POST'])
def login():
    return UserHandler().authorize(request.get_json('data'))


@app.route('/JEChat/Users')
def getUsers():
    users = UserHandler().getUsers()
    return users


@app.route('/JEChat/Messages', methods=['GET', 'POST'])
def getMessages():
    return MessagesHandler().getMessages()


@app.route('/JEChat/Users/<int:usrid>/Messages')
def getUserMessagesById(usrid):
    return MessagesHandler().getUserMessagesById(usrid)


@app.route('/JEChat/<name>/Messages/<int:mid>/likes', methods=['GET', 'POST'])
def getMessageLikes(name, mid):
    if request.method == 'POST':
        return MessagesHandler().insertLikes(request.get_json('data'))
    else:
        return MessagesHandler().getMessageLikes(name, mid)


@app.route('/JEChat/<gid>/Messages/<int:mid>/dislikes', methods=['GET', 'POST'])
def getMessageDislikes(gid, mid):
    if request.method == 'POST':
        return MessagesHandler().insertDislikes(request.json)
    return MessagesHandler().getMessageDislikes(gid, mid)


@app.route('/JEChat/<gid>/Messages/<int:mid>/replies', methods=['GET', 'POST'])
def getMessageReplies(gid, mid):
    if request.method == 'POST':
        return MessagesHandler().insertReply(request.json)
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


@app.route('/JEChat/<int:usrid>/GroupChats', methods=['GET', 'POST'])
def getUserGroupchats(usrid):
    if request.method == 'POST':
        return GroupChatHandler().insertGroup(request.get_json('data'), usrid)
    else:
        return GroupChatHandler().getUserGroupchats(usrid)


@app.route('/JEChat/<int:usrid>/GroupChats/<groupname>', methods=['GET', 'POST'])
def getUserGroupContent(usrid, groupname):
    if request.method == 'POST':
        return MessagesHandler().insertMessage(request.get_json('data'), usrid, groupname)
    else:
        return GroupChatHandler().getUserGroupContent(usrid, groupname)


@app.route('/JEChat/<int:usrid>/GroupChats/<groupname>/reactionlikes')
def getUserGroupReactions(usrid, groupname):
    return GroupChatHandler().getUGMLikes(usrid, groupname)


@app.route('/JEChat/<int:usrid>/ContactList', methods=['GET', 'POST'])
def getContactsByUser(usrid):
    if request.method == 'POST':
        return AddressBook().addContact(request.get_json('data'), usrid)
    else:
        return AddressBook().getUserContacts(usrid)


@app.route('/JEChat/GroupChats/<int:gid>/Members', methods=['GET'])
def getUsersInGroup(gid):
    return GroupChatHandler().getUsersInGroup(gid)


@app.route('/JEChat/GroupChats/Members', methods=['POST'])
def addMember():
    if request.method == 'POST':
        return GroupChatHandler().insertMember(request.get_json('data'))
    return jsonify(ERROR='WRONG METHOD')


@app.route('/JEChat/Hashtags', methods=['POST'])
def getMessagesWithHashtag():
    if request.method == 'POST':
        return HashtagHandler().getMessagesWithHashtags(request.get_json('data'))
    else:
        return jsonify(ERROR='WRONG METHOD')


""" Routes for Dashboard Functionality """
"""----------------------------------------------------START"""
@app.route('/JEChat/messages/countperday')
def MessagesPerDay():
    return Dashboard().MessagesPerDay()


@app.route('/JEChat/likes/countperday')
def LikesPerDay():
    return Dashboard().LikesPerDay()


@app.route('/JEChat/dislikes/countperday')
def DislikesPerDay():
    return Dashboard().DislikesPerDay()


@app.route('/JEChat/replies/countperday')
def RepliesPerDay():
    return Dashboard().RepliesPerDay()


@app.route('/JEChat/hashtags/trend')
def TrendingHashtags():
    return Dashboard().TrendingHashtags()


@app.route('/JEChat/users/activity')
def ActiveUsers():
    return Dashboard().ActiveUsers()
"""-----------------------------------------------------END"""



# <------------------ Routes for User fetching actions

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
    return UserHandler().getUsersByUsername(username)
# End of User actions ------------------------------------------->
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


@app.route('/JEChat/GroupChats/<int:gid>/Admin')
def getGroupAdmin(gid):
    return GroupChatHandler().getGroupAdmin(gid)


@app.route('/JEChat/GroupChats/Names')
def getGroupNames():
    return GroupChatHandler().getAllGroupNames()
# End fo GroupChat fetching actions --------------------------->


# <---------------- Routes for Contact Lists actions
@app.route('/JEChat/ContactLists')
def getContactLists():
    return AddressBook().getContactLists()

# End of Contact List actions ------------------->
# <----------------------Routes for Hashtags actions

@app.route('/JEChat/TrendingHashtags')
def getHashtags():
    return MessagesHandler().getHashtags()


if __name__ == '__main__':
    app.run(port=4545)
