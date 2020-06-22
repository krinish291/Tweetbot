import tweepy
import time

consumer_key='X'
consumer_secret='X'
key='X-X'
secret='X'
 
#configuration

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth ,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
FILE_NAME='last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME,last_seen_id):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return 

#api.update_status('Twitter bot reporting live,Developed by Krinish.')


#Search and like

'''search="unsubscribetseries"
nr=100
for tweet in tweepy.Cursor(api.search,search).items(nr):
    try:
        print('Like')
        tweet.favorite()
        time.sleep(3)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break'''


def LikeAndRT():
    tweets=api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#tweetbot' in tweet.full_text.lower():
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME,tweet.id)


#Followback
'''def Followback():
    for follower in tweepy.Cursor(api.followers).items():
        time.sleep(5)
        if not follower.following:
            follower.follow()            
            print (follower.screen_name)'''

while True:
    LikeAndRT()
    #Followback()
    time.sleep(15)
