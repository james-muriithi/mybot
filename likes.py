import tweepy

consumer_key = ""
consumer_secret = ""

access_token = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,  wait_on_rate_limit=True)

queries = ["gloria", "ishasir"]

for q in queries:
    for tweet in tweepy.Cursor(api.search, q=q).items(5):
        print(tweet.text)
        try:
            tweet.retweet()
            tweet.favorite()
            print("You just Retweeted and liked the by ".format(tweet.user.name))
        except tweepy.TweepError as error:
            print(error.reason)


