import tweepy
import json

with open('twitter_credentials.json', 'r') as f:
    twitter_credentials = json.load(f)


class TwitterClient:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(twitter_credentials['CONSUMER_KEY'], twitter_credentials['CONSUMER_SECRET'])
        self.auth.set_access_token(twitter_credentials['ACCESS_TOKEN'], twitter_credentials['ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def get_friend_list(self, user, num_friends):
        friend_list = []
        for friend in tweepy.Cursor(self.api.friends, id=user).items(num_friends):
            friend_list.append(friend)
        return friend_list
