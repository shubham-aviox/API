import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("mydata.csv")
df.head()
print(df, 'sdjfkhdk')


coins = list(df.coin.unique())
print(coins)

people = list(df.rice.unique())
print(people)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))

# 1. Create the graph
g = nx.from_pandas_edgelist(df, source='rice', target='coin') 

# 2. Create a layout for our nodes 
layout = nx.spring_layout(g,iterations=50)

# 3. Draw the parts we want
nx.draw_networkx_edges(g, layout, edge_color='#AAAAAA')

Coins = [node for node in g.nodes() if node in df.coin.unique()]
size = [g.degree(node) * 80 for node in g.nodes() if node in df.coin.unique()]
nx.draw_networkx_nodes(g, layout, nodelist=Coins, node_size=size, node_color='lightblue')

people = [node for node in g.nodes() if node in df.rice.unique()]
nx.draw_networkx_nodes(g, layout, nodelist=people, node_size=100, node_color='#AAAAAA')

high_degree_people = [node for node in g.nodes() if node in df.rice.unique() and g.degree(node) > 1]
nx.draw_networkx_nodes(g, layout, nodelist=high_degree_people, node_size=100, node_color='#fc8d62')

club_dict = dict(zip(Coins, Coins))
nx.draw_networkx_labels(g, layout, labels=club_dict)

# 4. Turn off the axis because I know you don't want it
plt.axis('off')

plt.title("Revolutionary Coins")

# 5. Tell matplotlib to show it
# nx.write_gexf(g, "graph.csv")
size = [g.degree(node) * 80 for node in g.nodes() if node in df.coin.unique()]
nx.draw_networkx_nodes(g, layout, nodelist=Coins, node_size=size, node_color='red')
plt.savefig("filename.png")