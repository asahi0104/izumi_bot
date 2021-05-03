from twitter import *
from config import *
oauth_dance(APP_NAME, CONSUMER_KEY, CONSUMER_SECRET,
            token_filename="./config.txt", open_browser=False)
