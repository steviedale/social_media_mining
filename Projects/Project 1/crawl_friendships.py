import tweepy
import os
import pickle
import json

import twitter_credentials


class TwitterClient:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        self.auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def get_user_timeline_tweets(self, user, num_tweets):
        tweets = []
        for tweet in tweepy.Cursor(self.api.user_timeline, id=user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, user, num_friends):
        friend_list = []
        for friend in tweepy.Cursor(self.api.friends, id=user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, user, num_tweets):
        home_timeline_tweets = []
        for tweet in tweepy.Cursor(self.api.home_timeline, id=user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


def add_friends_recursive(graph, expanded_user_nodes, user_id, iterations_left):
    friends = twitter_client.get_friend_list(user=user_id, num_friends=1000)
    for friend in friends:

        if friend.name == user_id:
            continue

        if friend.name not in expanded_user_nodes:
            graph.add_node(friend.name)
            expanded_user_nodes[friend.name] = friend
            if iterations_left > 0:
                add_friends_recursive(
                    graph=graph,
                    expanded_user_nodes=expanded_user_nodes,
                    user_id=friend.id,
                    iterations_left=iterations_left-1
                )

        graph.add_edge(friend.name, user_id)
        print('{} -> {}'.format(user_id, friend.name))


if __name__ == '__main__':
    twitter_client = TwitterClient()
    users_already_crawled = [s.rstrip('.pickle') for s in os.listdir('users')]

    with open('users_to_add.json', 'r') as f:
        users_to_add = json.load(f)

    for user_id in users_to_add:
        if user_id in users_already_crawled:
            print('skipping {}...'.format(user_id))
            continue
        try:
            print('adding {}...'.format(user_id))
            friends = twitter_client.get_friend_list(user=user_id, num_friends=200)
            with open(os.path.join('users', user_id+'.pickle'), 'wb') as f:
                pickle.dump(friends, f)
            print('added!')
        except:
            print("FAILED")

    print('done')
