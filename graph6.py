import networkx as nx

def Graph():
    G = nx.Graph()
    
    k = 7
    
    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(1,5)
    G.add_edge(1,6)
    G.add_edge(2,3)
    G.add_edge(2,6)
    G.add_edge(2,7)
    G.add_edge(3,6)
    G.add_edge(4,5)
    G.add_edge(4,6)
    G.add_edge(5,6)
    G.add_edge(5,7)
    G.add_nodes_from(G.nodes(), colour='never coloured')
    return G
