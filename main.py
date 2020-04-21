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
        self.consumer_key = "xRdEidFY8tGyUk8bI1GNo3XeL"
        self.consumer_secret = "yQ1kqwtg0pveQKNXJCC7KrWuKeZeakM1615EhMdswSc2cUKrUi"
        self.access_token = "1184893494642561024-tkpuIBCreDuF5vOgBCz7ZG7TmEmrBH"
        self.access_token_secret = "5DgxAa5kElMMCO8libTH4GDKECdWRdQ6iKeiVfdEiHw8c"
        self.tweets = []
        self.jsonTweets = []
    
    ## TODO    
    def retreiveKeys(self, fileName):
        file = open(fileName)
        keys = []
        
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