import networkx as nx
import graph6
def find_next_vertex(G):
    adj=[]
    n = len(G.nodes())
    for i in range (1,n):
        if G.nodes[i]['visited']=='yes':
            adjacent=G.adj[i]
            for vertex in adjacent:
                if G.nodes[vertex]['visited']!='yes':
                    if vertex not in adj:
                        adj.append(vertex)
    adj.sort()
    return adj[0]

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
    visited_counter=1
    colour=find_smallest_colour(G,1)
    G.nodes[1]['colour']=colour
    G.nodes[1]['visited']='yes'
    while visited_counter<=n-1:
        visited_counter+=1
        i=find_next_vertex(G)
        print(i)
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


print('Graph G6:')
G=graph6.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


