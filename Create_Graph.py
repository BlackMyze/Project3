import networkx as nx
from Connections import Conexiones


# Listing the connections as a dictionary
nodes = dict(map(lambda node, Conexiones: (node, Conexiones[1:]) , list(map(lambda conec: conec[0], Conexiones)), Conexiones))
"""
{
    ip machine: [ ip_1, ..., ip_n ] 
}
"""

G = nx.Graph()

# Add each node (machine ip)
G.add_nodes_from(nodes.keys())

# Add edges to each node
for node, edges_list in nodes.items():
    G.add_edges_from( list(map(lambda edges_list: (node,edges_list), edges_list)) )

