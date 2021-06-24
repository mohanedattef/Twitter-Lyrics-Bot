import tweepy
from random import randint
import time


#get those from the twitter api
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
#standard api initializing 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#open the lyrics file and store it in a list/count lines/set the last line condition
rlyrics = open('lyrics2.txt', encoding='utf-8')
lyrics=rlyrics.readlines()
lastline = 0
lines=len(lyrics)
#seperate the identifer from the lyrics and add a line for styling, post the lyrics then sleep for an hour till it posts again
while True:
    gottenline = randint(1,lines)
    while gottenline == lastline:
        gottenline=randint(1,lines)
    tweet_text=lyrics[gottenline]
    tweet_text = tweet_text.replace("|", '\n')
    api.update_status(tweet_text)
    time.sleep(60*30*2)   

