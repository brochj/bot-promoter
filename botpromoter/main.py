# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:43:59 2020

@author: broch
"""

import tweepy
import time
# import random
# from pprint import pprint

from api.connection import Connection
from routines import Routines
from credentials import TOKENS
from texts.promote_trends import PromoteTrends
from texts.promote_user import PromoteUser
from texts.ham_artesanal import HamArtesanalTrends
from texts.ham_artesanal import HamArtesanalUser

api = Connection(TOKENS).connect()
# pprint(api.rate_limit_status()['resources'])

bot = Routines(api)
# bot.promote('curso online quero fazer', items=30)
# curso online quero fazer - 30 items - 05/02/21

# ham_artesanal_tweet = HamArtesanalTrends().getTweetMethod()
# bot.promote_on_trends(ham_artesanal_tweet)

# tweet = PromoteTrends().getTweetMethod()
# bot.promote_on_trends(tweet)

while True:
    bot.promote_on_trends()
    print('Waiting 40 minutes')
    time.sleep(40 * 60)
