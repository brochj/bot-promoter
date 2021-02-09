# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:03:29 2021

@author: broch
"""

import tweepy
import time
from datetime import datetime
# import random
# from pprint import pprint

from bot.create import CreateBot
from texts.promote_trends import PromoteTrends
from texts.promote_user import PromoteUser
from texts.ham_artesanal import HamArtesanalTrends


class Routines:
    def __init__(self, api):
        self.api = api
        self.bot = CreateBot(api)
        self.last_tweet = ""

    def promote(self, query, url='https://cursosinteressantes.com.br/', items=100):

        for tweet in tweepy.Cursor(self.api.search, query, lang='pt').items(items):
            print(f"Checking tweet from @ {tweet.user.screen_name}")

            tweet_method = PromoteUser().getTextMethod()
            tweet_text = tweet_method(user=tweet.user.screen_name)

            # Checks if I'm not replying to myself
            if self.api.me().id == tweet.user.id:
                print("I will not answer my own tweet\n")
                continue

            # Checks if will duplicate tweets
            if self.last_tweet == tweet_text:
                print("I will not create duplicated tweets\n")
                continue

            try:
                self.bot.actions.reply(tweet_text, tweet.id)
                self.print_tweet_sent(tweet_text)

                self.last_tweet = tweet_text
                time.sleep(30)

            except tweepy.TweepError as e:
                print(e.reason)
                time.sleep(10)
            except tweepy.RateLimitError:
                print('Limit reached, waiting 15 minutes...')
                time.sleep(15 * 60)
            except StopIteration:
                break

    def promote_to_user(self, query, tweet_method, items=100):
        for tweet in tweepy.Cursor(self.api.search, query, lang='pt').items(items):
            print(f"Checking tweet from @ {tweet.user.screen_name}")
            tweet_text = tweet_method(user=tweet.user.screen_name)

            # Checks if I'm not replying to myself
            if self.api.me().id == tweet.user.id:
                print("I will not answer my own tweet\n")
                continue

            # Checks if will duplicate tweets
            if self.last_tweet == tweet_text:
                print("I will not create duplicated tweets\n")
                continue

            try:
                self.bot.actions.reply(tweet_text, tweet.id)
                self.print_tweet_sent(tweet_text)
                self.last_tweet = tweet_text
                time.sleep(30)
            except tweepy.TweepError as e:
                print(e.reason)
                time.sleep(10)
            except tweepy.RateLimitError:
                print('Limit reached, waiting 15 minutes...')
                time.sleep(15 * 60)
            except StopIteration:
                break

    def promote_on_trends(self, step=2):
        trends = self.bot.search.trends()
        for i in range(0, len(trends), step):
            selected_trends = " ".join(trends[i:i + step])

            # tweet_method = PromoteTrends().getTweetMethod()
            tweet_method = HamArtesanalTrends().getTweetMethod()

            tweet_text = tweet_method(trends=selected_trends)
            self.try_send_tweet(tweet_text)

    def try_send_tweet(self, tweet_text):
        try:
            self.bot.actions.tweet(tweet_text)
            self.print_tweet_sent(tweet_text)
            time.sleep(40)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)
        except tweepy.RateLimitError:
            print('Limit reached, waiting 15 minutes...')
            time.sleep(15 * 60)

    def print_tweet_sent(self, tweet_text):
        width = 40
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("#" * width)
        print(f"Tweet Enviado! [{current_time}]".center(width))
        print("#" * width)
        print(tweet_text)
        print("#" * width + "\n")
