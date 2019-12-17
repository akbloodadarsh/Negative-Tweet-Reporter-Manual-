# Negative-Tweet-Reporter

#### Follow The Steps
### 1. Insert Your Twitter Credentials in TwitterCredentials.py
### 2. Run the test.py
### 3. Enter the hashtag you want to target.Ex:- #NameOfHashtag
### 4. Let the program fetch and analyse the tweets
### 5. When it will encouner a negative tweet it will ask for you to analyse the tweet and if in your perspective it is a negative tweet, you can press y to report it!
### 6. Then the process will resume

#### How this is happening

I have used training data to train a model using multinomial naive bayes,then we are fetching tweets 10 at a time(Their is a maximum limit of 3200 tweets).Then we are using our tained model to analyse the tweet and if it predicts that the tweet is negative we are asking the user to analyse the tweet and if from his perspective the tweet is negative he can verify it and the program will automatically report it!
The program is only fetching the tweets which are english!
