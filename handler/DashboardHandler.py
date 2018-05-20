from dao.DashboardDAO import *
from flask import jsonify


class Dashboard:

    def arrangeAlpha(self, row):
        return {'count': row[0], 'date': row[1]}

    def arrangeBeta(self, row):
        return {'count': row[0], 'date': row[1], 'user': row[2]}

    def arrangeCharlie(self, row):
        return {'hashtag': row[0], 'count': row[1]}

    def ActiveUsers(self):
        dao = DashboardDAO()
        result = dao.ActiveUsers()
        count = []
        if result:
            for r in result:
                count.append(self.arrangeBeta(r))
            return jsonify(Count=count)
        else:
            return jsonify(ERROR='Nothing in database')

    def MessagesPerDay(self):
        dao = DashboardDAO()
        result = dao.MessagesPerDay()
        count = []
        if result:
            for r in result:
                count.append(self.arrangeAlpha(r))
            return jsonify(Count=count)
        else:
            return jsonify(ERROR='No Messages in Database')

    def LikesPerDay(self):
        dao = DashboardDAO()
        result = dao.LikesPerDay()
        count = []
        if result:
            for r in result:
                count.append(self.arrangeAlpha(r))
            return jsonify(Count=count)
        else:
            return jsonify(ERROR='No likes in Database')

    def DislikesPerDay(self):
        dao = DashboardDAO()
        result = dao.DislikesPerDay()
        count = []
        if result:
            for r in result:
                count.append(self.arrangeAlpha(r))
            return jsonify(Count=count)
        else:
            return jsonify(ERROR='No dislikes in Database')

    def RepliesPerDay(self):
        dao = DashboardDAO()
        result = dao.RepliesPerDay()
        count = []
        if result:
            for r in result:
                count.append(self.arrangeAlpha(r))
            return jsonify(Count=count)
        else:
            return jsonify(ERROR='No replies in Database')

    def TrendingHashtags(self):
        dao = DashboardDAO()
        result = dao.TrendingHashtags()
        count = []
        if result:
            for r in result:
                count.append(self.arrangeCharlie(r))
            return jsonify(Count=count)
        else:
            return jsonify(ERROR='No hashtags in database')