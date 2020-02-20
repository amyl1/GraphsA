import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    potential=[]
    for i in range(1,len(G.nodes())):
        if G.nodes[i]['visited']=="yes":
            potential.append(G.nodes[i])
    print(potential)






def find_smallest_colour(G,i):
    n = len(G.nodes())
    neighbours=[]
    adjacent=G.adj[i]
    for vertex in adjacent:
        neighbours.append(G.nodes[vertex]['colour'])
    col=1
    while col in neighbours:
        col+=1
    return col


def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter











    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.node[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
print(find_next_vertex(G))
"""
print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
"""