""" API for twitter """

import tweepy
import re

consumer_key = "4zyqIx8iMixxDVCPjdQp6xxxxxxkvxhixKxi7" # input your keys in the next few lines
consumer_secret = "aRSXs313yO1kzE82L"
bearer_token = 'gEAAAAAFi2Kt3WAwMsaQVfS331PX92mOEFo8tvGWo'
access_token = '12153092-8dYAW0kM0lUaLF'
access_token_secret = 'hRNVg1A6LpgledHl4L34Lx8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

m = re.compile(r'screen_name\':\s\'([^\s])+')

user = api.get_user('yourname')

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)



