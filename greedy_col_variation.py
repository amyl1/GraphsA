import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

def find_next_vertex(G):
    visited=[]
    potential=[]
    possible=[]
    for i in range(1,len(G.nodes())):
        if G.nodes[i]['visited']=='yes':
            visited.append(i)
    for vertex in visited:
        adjacent=G.adj[vertex]
        potential.extend(adjacent)
    for x in range (0,(len(potential))):
        if G.nodes[potential[x]]['visited']!='yes':
            possible.append(potential[x])
    possible.sort()
    if len(possible)==0:
        possible.append(1)
    return possible[0]

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
    kmax=1
    global visited_counter
    visited_counter=0
    while visited_counter<=n-1:
        visited_counter+=1
        i=find_next_vertex(G)
        G.nodes[i]['visited']='yes'
        colour=find_smallest_colour(G,i)
        G.nodes[i]['colour']=colour
        if colour>kmax:
            kmax=colour

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()

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
