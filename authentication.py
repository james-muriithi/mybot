import tweepy

consumer_key = ""
consumer_secret = ""

access_token = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# to get the tweets in your home page
# tweets = api.home_timeline()
#
# for tweet in tweets:

    # print(tweet.text)



# to get my own tweets
my_tweets = api.user_timeline()

for tweet in my_tweets:
    print(tweet.text)






