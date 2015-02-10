import json
from pprint import pprint
import solr_util
import time
import datetime
from pytz import timezone
from datetime import datetime

def read_tweets():
    with open('tweets.json') as json_data:
        data = json.load(json_data)
        json_tweets = json.loads(data)

        for tweet in json_tweets:
            #remove multi-valued fields for now
            tweet['user_id'] = tweet['user']['id']
            tweet['user_screen_name'] = tweet['user']['screen_name']

            del tweet['user']

            tweet['urls'] = [url['url'] for url in tweet['entities']['urls']]
            tweet['hashtags'] = tweet['entities']['hashtags']

            #print t['entities']['user_mentions']

            del tweet['entities']

            del tweet['retweeted'] #don't need this if we have count
            del tweet['truncated']
            del tweet['id_str']
            del tweet['favorited']

            if 'possibly_sensitive' in tweet:
                del tweet['possibly_sensitive']

            if 'extended_entities' in tweet:
                del tweet['extended_entities']

            #del tweet['created_at']
            #fit the date format
            utc = timezone('UTC')
            print tweet['created_at']
            created_at = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')

            #"YYYY-MM-DDThh:mm:ssZ"
            tweet['created_at'] = created_at.strftime('%Y-%m-%dT%H:%M:%SZ')

            solr_util.post(tweet)

            """
            print t['created_at']
            print t['text']
            print  t['user']['id']
            print t['user']['screen_name']
            print t['id']
            print t['lang']
            print t['retweet_count']
            print t['contributors']
            print t['coordinates']
            print t['entities']['urls']
            print t['entities']['hashtags']
            print t['entities']['user_mentions']
            print t['favorite_count']
            print t['in_reply_to_user_id']
            print t['in_reply_to_status_id']
            """

        print "done"


if __name__=='__main__':
   read_tweets()
