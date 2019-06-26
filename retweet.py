import tweepy

consumer_key = ""
consumer_secret = ""

access_token = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,  wait_on_rate_limit=True)

for follower in tweepy.Cursor(api.followers).items(10):
    # print(follower.name)
    try:
        if not follower.following:
            follower.follow()
            print("You Just followed " + follower.name)
    except tweepy.TweepError as error:
        print(error.reason)
