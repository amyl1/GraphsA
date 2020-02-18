import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_colour(G,i):
    n = len(G.nodes())
    print(n)
    colours=[]
    for col in range (1,n+1):
        colours.append(col)
    return colours








def greedy(G):
    global kmax







    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.node[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)

G=graph1.Graph()
print (G)
print(find_smallest_colour(G,15))
"""
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
"""
