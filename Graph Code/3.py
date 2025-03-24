import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Nodes (Security Elements)
nodes = ["User", "Blockchain", "Node 1", "Node 2", "Node 3", "Validator"]
G.add_nodes_from(nodes)

# Edges (Connections)
edges = [("User", "Blockchain"), ("Blockchain", "Node 1"), ("Blockchain", "Node 2"), 
         ("Blockchain", "Node 3"), ("Node 1", "Validator"), ("Node 2", "Validator"), 
         ("Node 3", "Validator")]

G.add_edges_from(edges)

# Draw graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
plt.title("Blockchain-Based Security Framework")
plt.show()
