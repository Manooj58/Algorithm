import networkx as nx
import matplotlib.pyplot as plt

def avg_degree(g):
    n = g.nodes
    total_degree = 0
    for node in g.degree:
        total_degree += node[1]
    avg = total_degree/len(n)
    return avg

def density(g):
    if len(g.nodes) > 1:
        density = 2*len(g.edges) / (len(g.nodes) * (len(g.edges)-1))
    else:
        density = 0
    return density

def diameter(g):
    if nx.is_connected(g) == False:
        return False
    d = 0
    for i in g.nodes:
        for j in g.nodes:
            if i == j:
                continue
            length = nx.shortest_path_length(g, source = i, target = j)
            if length > d:
                d = length
    return d

def calculate_clustering(graph):
    cluster = 0
    for i in graph.nodes:
        k = list(nx.neighbors(graph, i))
        e = 0
        for j in k:
            for i in k:
                if nx.is_path(graph, [j,i]):
                    e += 1
        if len(k) > 1:
            cluster += (2*(e/2))/ (len(k) * (len(k)-1))
    c = cluster / len(graph.nodes)
    return c

def degree_distribution(g):
    nodes = g.nodes
    maxDegree = max(y for x,y in g.degree)
    degree = [0 for _ in range(0, maxDegree+1)]
    for (x,y) in g.degree:
        degree[y] += 1
    for i in range(0, len(degree)):
        degree[i] = round(degree[i] / len(nodes), 2)
    return degree


def plotter(y):
    x = [0 for _ in range(0, len(y))]
    for i in range(0, len(x)):
        x[i] = i
    plt.plot(x,y)
    plt.show()
    return