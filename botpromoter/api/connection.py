# -*- coding: utf-8 -*-
import tweepy


class Connection:
    def __init__(self, tokens: dict):
        self.api = None
        self.consumer_key = tokens['CONSUMER_KEY']
        self.consumer_secret = tokens['CONSUMER_SECRET']
        self.access_token = tokens['ACCESS_TOKEN']
        self.access_token_secret = tokens['ACCESS_TOKEN_SECRET']

    def connect(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        return self.api
