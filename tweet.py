from twitter import *
from config import *
t = Twitter(
    auth=OAuth(
        '1389125351612186627-vZfttNRJbL87zKrSHJyKvtAjbLcrbM',  # token（config.txtの1行目）
        'nfizqBaX2MTAja2er5ZqcZnTbajI00YTljL3dzLY6Q7Pl',  # token_secret（config.txtの2行目）
        CONSUMER_KEY,
        CONSUMER_SECRET,
    )
)
t.statuses.update(status="test tweet from python.")
