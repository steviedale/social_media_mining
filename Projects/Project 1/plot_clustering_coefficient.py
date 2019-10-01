import networkx
import matplotlib.pyplot as plt
from network import get_network_graph

# ** IMPORTANT **
# set CRAWL_DATA to False to skip the crawling portion of this app (data is pre-loaded into pickle files under "users")
CRAWL_DATA = False

graph = get_network_graph(crawl_data=CRAWL_DATA)

cluster_coefficient_dict = networkx.clustering(graph)
cluster_coefficient_list = cluster_coefficient_dict.values()

# -- Plot Clustering Coefficient Distribution --
plt.title('Clustering Coefficient Distribution')
plt.xlabel('Clustering Coefficient')
plt.ylabel('# Nodes')
plt.hist(cluster_coefficient_list, bins=100)
plt.show()

