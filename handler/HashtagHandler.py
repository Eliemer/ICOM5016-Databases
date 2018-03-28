from flask import *
from dao.HashtagDAO import *

class HashtagHandler:
    def sort(self, row):
        hashtags = {}
        hashtags['hid'] = row[0]
        hashtags['hashtag'] = row[1]
        return hashtags
