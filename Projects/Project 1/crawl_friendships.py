import pickle
import networkx
import os
from matplotlib import pyplot as plt
from twitter_client import TwitterClient


# Global variables
expanded_user_ids = []
twitter_client = TwitterClient()


def recursive_add_friend_nodes(graph, user_id, screen_name, iterations_left):
    # get a list of friends for this user
    friend_objs = twitter_client.get_friend_list(user=user_id, num_friends=100)
    # turn the list of user objects into a list of minimal information (id and screen name)
    friend_dict = {friend.id_str: friend.screen_name for friend in friend_objs}
    # store the friends list in a .pickle file
    with open(os.path.join('user_pickles', '{}.pickle'.format(user_id)), 'wb') as f:
        pickle.dump(friend_dict, f)
    # iterate friends
    for friend_obj in friend_objs:
        # add this edge to the graph
        graph.add_edge(screen_name, friend_obj.screen_name)
        # if this user has already been expanded
        if friend_obj.id_str not in expanded_user_ids:
            # add this node to the graph
            graph.add_node(friend_obj.screen_name)
            # add this friend to the list of expanded old_list_of_users so that we don't try to expand it again
            expanded_user_ids.append(friend_obj.id_str)
            # while we haven't gone to the full recursive depth
            if iterations_left > 0:
                # get this friends list of friends
                recursive_add_friend_nodes(
                    graph=graph,
                    user_id=friend_obj.id_str,
                    screen_name=friend_obj.screen_name,
                    iterations_left=iterations_left-1
                )


if __name__ == '__main__':
    graph = networkx.DiGraph()
    recursive_add_friend_nodes(graph=graph, user_id='1169829015768616961',
                               screen_name='steviedale_4', iterations_left=4)

    print('# of edges: {}'.format(graph.number_of_edges()))
    print('# of nodes: {}'.format(graph.number_of_nodes()))

    clusters = networkx.clustering(graph)

    # pos = networkx.layout.spring_layout(graph)
    pos = networkx.layout.bipartite_layout(graph)

    nodes = networkx.draw_networkx_nodes(graph, pos, node_size=20)
    edges = networkx.draw_networkx_edges(graph, pos)

    ax = plt.gca()
    ax.set_axis_off()
    plt.show()
