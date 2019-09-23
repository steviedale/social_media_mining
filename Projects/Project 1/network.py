import networkx
import pickle

with open('all_users.pickle', 'rb') as f:
    all_users = pickle.load(f)

print('done')

graph = networkx.Graph()

