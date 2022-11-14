import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


access_key = "1591523602586746881-dNrJqEkt4DSn2i21jQcGqCizNVaUeh"
access_secret = "PVIuEYL4MLFY3TbUja7yOBAXYoCJiOX9hLg66pEvkpQfk"
consumer_key = "1MGkGkZ01bghv2WSRlCUUCvZA"
consumer_secret = "BoRNSpx1dV7Xa8j9PfDzlCg7kfWrRrauEMTnvzCNPvE7HKpmXt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.Client(auth)

tweets = api.get_users_tweets(id='@elonmusk')

print(tweets)







