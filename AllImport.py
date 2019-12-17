from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import API
import pandas as pd
import twitter_credentials
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# importing algorithms from our modules
import MultinomialNaiveBayes

# To pre-process the raw tweet text into useful information
import PreProcess
pp = PreProcess

# All Algorithms Object
mnb = MultinomialNaiveBayes