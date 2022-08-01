import tweepy
import json



### CLIENT AUTH MODULE ###

auth_paramethers = []

auth_file = open("auth.json")
auth_value = json.loads(auth_file.read())

for value in auth_value.values():
    auth_paramethers.append(value)
auth_file.close()

BEARER_TOKEN = auth_paramethers[0]
CONSUMER_KEY = auth_paramethers[1]
CONSUMER_SECRET = auth_paramethers[2]
ACCESS_TOKEN = auth_paramethers[3]
ACCESS_TOKEN_SECRET = auth_paramethers[4]

# authenticator = tweepy.OAuth1UserHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)



### API REQUEST MODULE ###

tweet_text = "Hello World!"
client.create_tweet(text=tweet_text)