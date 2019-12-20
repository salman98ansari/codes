#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:38:27 2019

@author: salman
"""
import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import re

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

data = pd.read_csv('Final_data_with_location.csv')
data['polarity'] = 'NaN'
data = data.values

for i in range(data.shape[0]):
    text = data[i][1]
    analysis = TextBlob(clean_tweet(data[i][1]), analyzer=NaiveBayesAnalyzer())
    pol = analysis.sentiment.classification
    print(i , pol)
    data[i][5] = pol

data = pd.DataFrame(data)
data.rename(columns = {
        '0': "date",
        '1': "tweet", 
        '2': "hashtags",
        '3': "city",
        '4': "state",
        '5': "polarity"
        }, inplace = True)
data.to_csv("Final_data_with_location_and_polarity.csv")
