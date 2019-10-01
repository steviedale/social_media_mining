import networkx
import matplotlib.pyplot as plt
from network import get_network_graph

# ** IMPORTANT **
# set CRAWL_DATA to False to skip the crawling portion of this app (data is pre-loaded into pickle files under "users")
CRAWL_DATA = False

graph = get_network_graph(crawl_data=CRAWL_DATA)

degree_dict = dict(networkx.degree(graph))
degree_list = degree_dict.values()

# -- Plot Network --
# get colors for each node base on its degree
colors = []
for user_id, degree in degree_dict.items():
    if degree == 1:
        colors.append('r')
    elif degree < 4:
        colors.append('b')
    elif degree < 10:
        colors.append('g')
    else:
        colors.append('y')
# layout for network plot
network_layout = networkx.layout.fruchterman_reingold_layout(graph)
# nodes on plot
nodes = networkx.draw_networkx_nodes(graph, network_layout, node_size=50, node_color=colors)
# edges on plot
edges = networkx.draw_networkx_edges(graph, network_layout)
# axis
ax = plt.gca()
ax.set_axis_off()
plt.show()

