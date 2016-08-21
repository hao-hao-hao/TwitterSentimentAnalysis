import tweepy

class Twitter_helper:
    consumer_key = "Enter your one"
    consumer_secret = "Enter your one"
    access_token = "Enter your one"
    access_token_secret = "Enter your one"
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    @staticmethod
    def search_tweets(query, count):
        tweets = []
        max_id = ""
        try:
            while len(tweets)<count:
                results = Twitter_helper.api.search(q=query,lang="en",count=count,max_id = max_id)
                max_id = results.max_id
                for result in results:
                    if len(tweets) >=count:
                        break
                    tweet = Tweet(result)
                    tweets.append(tweet)
                    print(len(tweets))
        except:
             print("Twitter API Error:" + len(tweets))
        return tweets

class Tweet:
    text = ""
    time = ""
    polarity=""
    subjectivity=""

    def __init__(self, object):
        self.text = getattr(object,"text")
        created_at = getattr(object,"created_at")
        self.time = str(created_at.year)+"/"+str(created_at.month) + "/" +str(created_at.day)
        s = 123