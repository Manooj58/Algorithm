
import networkx as nx
import functions


# graph = nx.read_edgelist("DD21.edges", nodetype=int, data=(("Type", str),))
# graph = nx.read_edgelist("ENZYMES_g117.edges",
#                          nodetype=int, data=(("Type", str),))
# graph = nx.read_edgelist("3elt.mtx", nodetype=int, data=(("Type", str),))
# graph = nx.read_edgelist("power.mtx", nodetype=int, data=(("Type", str),))
# graph = nx.read_edgelist("bcspwr10.mtx", nodetype=int, data=(("Type", str),))
graph = nx.read_edgelist(
    "model3.mtx", nodetype=int, data=(("Type", str),))

# graph = nx.read_edgelist(
#     "mammalia-voles-bhp-trapping-55.edges", nodetype=int, data=(("Type", str),))

print(f"Number of Nodes = {len(graph.nodes)}")
print(f"Number of Edges = {len(graph.edges)}")
print(f"Average degree = {functions.avg_degree(graph)}")
print(f"density = {functions.density(graph)}")
# print(f"diameter = {functions.diameter(graph)}")
print(f"clustering coefficient = {functions.calculate_clustering(graph)}")
y = functions.degree_distribution(graph)
functions.plotter(y)
