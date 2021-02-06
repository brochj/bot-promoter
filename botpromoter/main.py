# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:43:59 2020

@author: broch
"""

import tweepy
# import time
# import random
# from pprint import pprint

from api.connection import Connection
from routines import Routines
from credentials import TOKENS

api = Connection(TOKENS).connect()
# pprint(api.rate_limit_status()['resources'])

bot = Routines(api)
# bot.promote('curso online quero fazer', items=30)
bot.promote_on_trends()

# curso online quero fazer - 30 items - 05/02/21
