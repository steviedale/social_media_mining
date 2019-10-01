import networkx
import matplotlib.pyplot as plt
from network import get_network_graph

# ** IMPORTANT **
# set CRAWL_DATA to False to skip the crawling portion of this app (data is pre-loaded into pickle files under "users")
CRAWL_DATA = False

graph = get_network_graph(crawl_data=CRAWL_DATA)

page_rank_dict = networkx.pagerank(graph)
page_rank_list = page_rank_dict.values()

# -- Plot Page Rank Distribution --
plt.title('Page Rank Distribution')
plt.xlabel('Page Rank')
plt.ylabel('# Nodes')
plt.hist(page_rank_list, bins=100)
plt.show()
