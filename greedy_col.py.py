import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

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
    global kmax
    kmax=1
    for vertex in G.nodes:
        colour=find_smallest_colour(G,vertex)
        G.nodes[vertex]['colour']=colour
        if colour>kmax:
            kmax=colour

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)

