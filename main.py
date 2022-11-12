import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


access_key = "ZWRt6CP9UQTUk1o2RpZVuh9NA"
access_secret = "089yhcMsoig2FmukPCQWnW6rZ0vV5SOPSmNFeyzB6C7mtrod5U"
consumer_key = "1591523602586746881-PhiiXlw0pHAsJlW8csEqgSEWQu9Ev1"
consumer_secret = "TId7WrdrqWlqJ5VgpoCl6haxup4AZT8UTWiz2hlYliFdP"

auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                           count=25,
                           include_rts = False,
                           tweet_mode= 'extended')

print(tweets)





