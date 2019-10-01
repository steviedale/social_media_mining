import pickle
import os
from twitter_client import TwitterClient


twitter_client = None
user_ids_expanded = None


def recursive_friendship_crawl(user_id, screen_name, iterations_left, max_friends_per_node=100):

    global twitter_client, user_ids_expanded

    if twitter_client is None:
        twitter_client = TwitterClient()
    if user_ids_expanded is None:
        user_ids_expanded = []

    # get a list of friends for this user
    friend_objs = twitter_client.get_friend_list(user=user_id, num_friends=max_friends_per_node)
    # turn the list of user objects into a list of minimal information (id and screen name)
    friend_list = {
        friend.id_str: {
            'id': friend.id_str,
            'screen_name': friend.screen_name
        }
        for friend in friend_objs
    }
    # create a dictionary to store this user's list of friends
    user_dict = {
        'id': user_id,
        'screen_name': screen_name,
        'friends': friend_list
    }
    # store the friends list in a .pickle file
    with open(os.path.join('users', '{}.pickle'.format(user_id)), 'wb') as f:
        pickle.dump(user_dict, f)
    # iterate friends
    for friend_obj in friend_objs:
        # if this user has already been expanded
        if friend_obj.id_str not in user_ids_expanded:
            # add this friend to the list of expanded old_list_of_users so that we don't try to expand it again
            user_ids_expanded.append(friend_obj.id_str)
            # while we haven't gone to the full recursive depth
            if iterations_left > 1:
                # get this friends list of friends
                recursive_friendship_crawl(
                    user_id=friend_obj.id_str,
                    screen_name=friend_obj.screen_name,
                    iterations_left=iterations_left-1
                )
