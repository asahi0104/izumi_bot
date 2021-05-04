import tweepy
import datetime
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


def retweet_izumi(IDOL, LIMIT, max_id='', since='', until=''):
    id = ''
    IDOL = IDOL + ' -filter:retweets'
    # セッションを確立し、アイドル名でつぶやきを最大数検索
    api = session_establish()
    try:
        egoistic_sailor = api.search(
            q=IDOL, count=LIMIT, max_id=max_id, since=since, until=until)
    except tweepy.TweepError as e:
        api.update_status("検索に失敗しちゃったみたい。")
        print(e)

    for tweet in egoistic_sailor:
        try:
            id = tweet.id
            if max_id == id:
                continue
            else:
                print(id)
                api.retweet(id)
        except tweepy.TweepError as e:
            print("リツイートの処理に失敗しちゃったみたい。")
            print(e)
    return id


# メイン処理
IDOL_NAME = '大石泉'
max_id = ''
today = datetime.date.today().strftime('%Y-%m-%d')
start_time = '_00:00:00_JST'
end_time = '_23:59:59_JST'
since = str(today) + start_time
until = str(today) + end_time

while True:
    max_id = retweet_izumi(IDOL_NAME, SEARCH_LIMIT_COUNT, max_id, since, until)

    if max_id == '':
        break
