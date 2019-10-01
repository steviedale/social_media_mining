import networkx
import friendship_crawler
import os
import pickle


def get_network_graph(crawl_data=True):
    if crawl_data:
        # grab information from twitter about steviedale4's friendship network
        friendship_crawler.recursive_friendship_crawl(user_id='1169829015768616961',
                                                      screen_name='steviedale4', iterations_left=2,
                                                      max_friends_per_node=100)

    '''
    user_friendship_dict will have the following structure:
    {
        ID_OF_USER_A: {
            "id": ID_OF_USER_A,
            "screen_name": SCREEN_NAME_OF_USER_A,
            "friends": {
                ID_OF_FRIEND_1_OF_USER_A : {
                    "id": ID_OF_FRIEND_1_OF_USER_A,
                    "screen_name": SCREEN_NAME_OF_FRIEND_2_OF_USER_A
                },
                ID_OF_FRIEND_2_OF_USER_A: {
                    "id": ID_OF_FRIEND_2_OF_USER_A,
                    "screen_name": SCREEN_NAME_OF_FRIEND_2_OF_USER_A
                },
                ...
            }
        }
         ID_OF_USER_B: {
            "id": ID_OF_USER_B,
            "screen_name": SCREEN_NAME_OF_USER_B,
            "friends": {
                ID_OF_FRIEND_1_OF_USER_B : {
                    "id": ID_OF_FRIEND_1_OF_USER_B,
                    "screen_name": SCREEN_NAME_OF_FRIEND_2_OF_USER_B
                },
                ID_OF_FRIEND_2_OF_USER_B: {
                    "id": ID_OF_FRIEND_2_OF_USER_B,
                    "screen_name": SCREEN_NAME_OF_FRIEND_2_OF_USER_B
                },
                ...
            }
        }
    }
    '''
    user_friendship_dict = {}
    pickle_folder = 'users'
    for file_name in os.listdir(pickle_folder):
        with open(os.path.join(pickle_folder, file_name), 'rb') as f:
            '''
                "user_dict" is the variable pickled in each of the .pickle files. These variables (one per file) will have the
                following structure:
                {
                "id": ID_OF_USER,
                "screen_name": SCREEN_NAME_OF_USER,
                "friends": {
                ID_OF_FRIEND_1_OF_USER : {
                "id": ID_OF_FRIEND_1_OF_USER,
                "screen_name": SCREEN_NAME_OF_FRIEND_2_OF_USER
                },
                ID_OF_FRIEND_2_OF_USER: {
                "id": ID_OF_FRIEND_2_OF_USER,
                "screen_name": SCREEN_NAME_OF_FRIEND_2_OF_USER
                },
                ...
                }
                }
                '''
            user_dict = pickle.load(f)
        user_friendship_dict[user_dict['id']] = user_dict

    def add_user_to_graph(graph, user):
        if user not in graph:
            graph.add_node(user)
        else:
            print('user {} already in graph!'.format(user))

    # create a directed graph
    graph = networkx.DiGraph()

    for user_id, user_dict in user_friendship_dict.items():
        user_screen_name = user_dict['screen_name']
        add_user_to_graph(graph=graph, user=user_screen_name)
        for friend_id, friend_dict in user_dict['friends'].items():
            friend_screen_name = friend_dict['screen_name']
            add_user_to_graph(graph=graph, user=friend_screen_name)
            graph.add_edge(user_screen_name, friend_screen_name)

    return graph
