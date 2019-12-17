import sys
from AllImport import *
import time
from tkinter import *


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

# To authenticate and access the twitter


class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


# get all the data of the tweets and,pass only tweets text to preprocess and finally returns only the processed tweets
def process(data):
    temp = []
    for text in data['sentence']:
        text = pp.pre_processing(text)
        temp.append(text)
    data['sentence'] = temp
    return data['sentence']


def execute(hashtag):
    try:
        num_tweets = 10
        twitter_client = TwitterClient()
        api = twitter_client.get_twitter_client_api()
        tweets = Cursor(api.search, q=hashtag, rpp=100).items(num_tweets)
        datafile = pd.read_csv('Train.csv', sep=',', encoding="utf-8")
        x = process(datafile)
        y = datafile['label']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
        vector = CountVectorizer()
        vector.fit(x_train)
        x_train_vft = vector.transform(x_train)
        x_test_vft = vector.transform(x_test)
        for tweet in tweets:
            if tweet.lang == 'en':
                text = [pp.pre_processing(tweet.text)]
                vec = vector.transform(text)
                temp = mnb.MultinomialNBAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
                if temp == 'Negative':
                    print('Negative Tweet Encountred\n')
                    print(tweet.text)
                    print('Do you want to report this person\n')
                    print('Press y to report else press any key to continue')
                    choice = str(input())
                    if choice == 'y':
                        print('Person Reported\n')
                        user = tweet.entities.get('user_mentions')
                        name = str((user[0].get('screen_name')))
                        api.report_spam(screen_name=name)
                    for i in range(3):
                        print('....')
                        time.sleep(1)

    except Exception as e:
        # Print the error
        print(e)

        # When reach the rate limit
        def on_limit(self, track):
            # Print rate limiting error
            print("Rate limited, continuing")
            # Continue mining tweets
            return True
        # When timed out

        def on_timeout(self):
            # Print timeout message
            print(sys.stderr, 'Timeout')
            # Wait 10 seconds
            time.sleep(10)
            # Return nothing
            return True


if __name__ == '__main__':
    TotalTweets = 0
    print('Enter the hashtag you want to check and report\n')
    hashtag = str(input())
    while TotalTweets != 3200:
        print('fetching tweets please wait\n')
        time.sleep(3)
        execute(hashtag)
        TotalTweets += 10
