# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:43:06 2020

@authors: Michael Johansen, Brian Lin
"""

import tweepy as tw
import pandas as pd
from datetime import datetime, timedelta
from flask import Flask
import time
import json
app = Flask(__name__)

@app.route("/myTweets")
def main():
    TR = TweetRetreiver()
    myTweet = TR.retreiveTweets()
    return myTweet

class TweetRetreiver:
    def __init__(self):
        self.retreiveKeys('API-Keys.txt')
        self.tweets = []
        self.jsonTweets = []
    
    
    def retreiveKeys(self, fileName):
        fileLines = open(fileName).read().splitlines()
        self.consumer_key = fileLines[0]
        self.consumer_secret = fileLines[1]
        self.access_token = fileLines[2]
        self.access_token_secret = fileLines[3]
        
    def retreiveTweets(self):
        auth = tw.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)

        search = "*"
        
        targetDate = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')
        self.tweets = tw.Cursor(api.search,
              q=search,
              lang="en",
              geocode="43.1566,-77.6088,10km",
              since=targetDate).items(1)
        
        self.jsonTweets = [tweet._json for tweet in self.tweets]
        return self.jsonTweets[0]['text']
            
        
            
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #main()