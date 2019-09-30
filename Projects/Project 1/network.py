import networkx
import json
import matplotlib.pyplot as plt

with open('user_id_to_screen_name.json', 'r') as f:
    user_id_to_screen_name = json.load(f)

with open('user_friend_dict.json', 'r') as f:
    user_friend_dict = json.load(f)

graph = networkx.DiGraph()

expanded_users = list(user_friend_dict.keys())

user_nodes_added = []
for user_id, friend_list in user_friend_dict.items():
    user_screen_name = user_id_to_screen_name[user_id]
    if user_screen_name not in user_nodes_added:
        user_nodes_added.append(user_screen_name)
        graph.add_node(user_screen_name)
    for friend_id in friend_list:
        if friend_id in expanded_users:
            friend_screen_name = user_id_to_screen_name[friend_id]
            if friend_screen_name not in user_nodes_added:
                user_nodes_added.append(friend_screen_name)
                graph.add_node(friend_screen_name)
            graph.add_edge(user_screen_name, friend_screen_name)

print('# of edges: {}'.format(graph.number_of_edges()))
print('# of nodes: {}'.format(graph.number_of_nodes()))

clusters = networkx.clustering(graph)


pos = networkx.layout.bipartite_layout(graph)

nodes = networkx.draw_networkx_nodes(graph, pos, node_size=20)
edges = networkx.draw_networkx_edges(graph, pos)

ax = plt.gca()
ax.set_axis_off()
plt.show()
