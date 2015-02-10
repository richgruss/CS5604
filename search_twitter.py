import oauth2 as oauth
import json

CONSUMER_KEY = 'eUS3osDalsgvD9mBG1wa7PbJn'
CONSUMER_SECRET='mnCCvShvA79noQYJ0n3VyHh92I3PVuRJgxtTeTzlpURzUQV7D4'
ACCESS_KEY = '151100545-vQlEKDRsNuLiUVtMi7KGCfP3VbBTHEWjf6GZuFaO'
ACCESS_SECRET = 'cDmfU8M5tiFXkr2SFwxeYWgCQ1rxQiIAQTaJFl0pmH8J4'

def search_twitter():
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth.Client(consumer, access_token)

    timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    response, data = client.request(timeline_endpoint)

    outfile = open('tweets.json', 'w')
    json.dump(data, outfile)

if __name__=='__main__':
    search_twitter()







