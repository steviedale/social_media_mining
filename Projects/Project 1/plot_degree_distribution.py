import networkx
import matplotlib.pyplot as plt
from network import get_network_graph

# ** IMPORTANT **
# set CRAWL_DATA to False to skip the crawling portion of this app (data is pre-loaded into pickle files under "users")
CRAWL_DATA = False

graph = get_network_graph(crawl_data=CRAWL_DATA)

degree_dict = dict(networkx.degree(graph))
degree_list = degree_dict.values()

# -- Plot Degree Distribution --
plt.title('Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('# Nodes')
plt.hist(degree_list, bins=100)
plt.show()


# -- Plot Clustering Coefficient --
cluster_coefficient_dict = networkx.clustering(graph)
