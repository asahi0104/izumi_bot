import json
import datetime
import time
import math
from requests_oauthlib import OAuth1Session
from twitter import *
from config import *
from pytz import timezone
from dateutil import parser

# 定数定義
SEARCH_TWEETS = 'https://api.twitter.com/1.1/search/tweets.json'
RATE_LIMIT_STATUS = "https://api.twitter.com/1.1/application/rate_limit_status.json"
IZUMI = '大石泉'


# セッション確立
def session_establish():
    return OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# ツイート取得
