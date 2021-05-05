import tweepy
import datetime
import time
from config import *
from pprint import pprint

# 定数定義
SEARCH_LIMIT_COUNT = 100  # APIの制限


def session_establish():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    return api


def retweet_izumi(IDOL, LIMIT, since='', until='', result_type=''):
    id = 0
    # セッションを確立し、アイドル名でつぶやきを最大数検索
    api = session_establish()
    try:
        egoistic_sailor = api.search(
            q=IDOL, count=LIMIT, since=since, until=until, result_type=result_type)
    except tweepy.TweepError as e:
        api.update_status("検索に失敗しちゃったみたい。")
        print(e)

    for tweet in egoistic_sailor:
        print(tweet.created_at)
        try:
            if id < int(tweet.id):
                id = tweet.id
            api.retweet(tweet.id)
            print('リツイートしたよ。')
        except tweepy.TweepError as e:
            print("リツイートの処理に失敗しちゃったみたい。")
            print(e)
    return id


# メイン処理
IDOL_NAME = '大石泉'
max_id = ''
today = datetime.date.today().strftime('%Y-%m-%d')
result_type = 'recent'  # 最新のつぶやきを取得

while True:
    end_time = datetime.datetime.now()  # 現在時刻
    start_time = end_time - datetime.timedelta(hours=1)  # 1時間前
    since = str(today) + start_time.strftime('_%H:%M:%S_JST')
    until = str(today) + end_time.strftime('_%H:%M:%S_JST')

    time.sleep(30)
    max_id = retweet_izumi(IDOL_NAME, SEARCH_LIMIT_COUNT,
                           since, until, result_type)
    print(max_id)
