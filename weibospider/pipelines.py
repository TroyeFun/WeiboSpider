# -*- coding: utf-8 -*-
import pymongo
from pymongo.errors import DuplicateKeyError
from settings import MONGO_HOST, MONGO_PORT
import json


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        db = client['weibo']
        self.Users = db["Users"]
        self.Tweets = db["Tweets"]
        self.Comments = db["Comments"]
        self.Relationships = db["Relationships"]

    def process_item(self, item, spider):
        if spider.name == 'comment_spider':
            self.insert_item(self.Comments, item)
        elif spider.name == 'fan_spider':
            self.insert_item(self.Relationships, item)
        elif spider.name == 'follower_spider':
            self.insert_item(self.Relationships, item)
        elif spider.name == 'user_spider':
            self.insert_item(self.Users, item)
        elif spider.name == 'tweet_spider':
            self.insert_item(self.Tweets, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            pass


class JsonPipeline(object):
    def __init__(self):
        self.f = open('./data/data.json', 'w')
        self.flush_freq = 100
        self.count = 0

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.f.write(content)
        self.count += 1
        if self.count % self.flush_freq == 0:
            self.f.flush()
        return item