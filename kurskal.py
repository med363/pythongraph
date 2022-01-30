import networkx as nx
import matplotlib.pyplot as plt


# # Python program for Kruskal's algorithm to find
# # Minimum Spanning Tree of a given connected,
# # undirected and weighted graph
 
# from collections import defaultdict
 
# # Class to represent a graph
 
 
# class Graph:
 
#     def __init__(self, vertices):
#         self.V = vertices  # No. of vertices
#         self.graph = []  # default dictionary
#         # to store graph
 
#     # function to add an edge to graph
#     def addEdge(self, u, v, w):
#         self.graph.append([u, v, w])
 
#     # A utility function to find set of an element i
#     # (uses path compression technique)
#     def find(self, parent, i):
#         if parent[i] == i:
#             return i
#         return self.find(parent, parent[i])
 
#     # A function that does union of two sets of x and y
#     # (uses union by rank)
#     def union(self, parent, rank, x, y):
#         xroot = self.find(parent, x)
#         yroot = self.find(parent, y)
 
#         # Attach smaller rank tree under root of
#         # high rank tree (Union by Rank)
#         if rank[xroot] < rank[yroot]:
#             parent[xroot] = yroot
#         elif rank[xroot] > rank[yroot]:
#             parent[yroot] = xroot
 
#         # If ranks are same, then make one as root
#         # and increment its rank by one
#         else:
#             parent[yroot] = xroot
#             rank[xroot] += 1
 
#     # The main function to construct MST using Kruskal's
#         # algorithm
#     def KruskalMST(self):
 
#         result = []  # This will store the resultant MST
         
#         # An index variable, used for sorted edges
#         i = 0
         
#         # An index variable, used for result[]
#         e = 0
 
#         # Step 1:  Sort all the edges in
#         # non-decreasing order of their
#         # weight.  If we are not allowed to change the
#         # given graph, we can create a copy of graph
#         self.graph = sorted(self.graph,
#                             key=lambda item: item[2])
 
#         parent = []
#         rank = []
 
#         # Create V subsets with single elements
#         for node in range(self.V):
#             parent.append(node)
#             rank.append(0)
 
#         # Number of edges to be taken is equal to V-1
#         while e < self.V - 1:
 
#             # Step 2: Pick the smallest edge and increment
#             # the index for next iteration
#             u, v, w = self.graph[i]
#             i = i + 1
#             x = self.find(parent, u)
#             y = self.find(parent, v)
 
#             # If including this edge does't
#             #  cause cycle, include it in result
#             #  and increment the indexof result
#             # for next edge
#             if x != y:
#                 e = e + 1
#                 result.append([u, v, w])
#                 self.union(parent, rank, x, y)
#             # Else discard the edge
 
#         minimumCost = 0
#         print ("Edges in the constructed MST")
#         for u, v, weight in result:
#             minimumCost += weight
#             print("%d -- %d == %d" % (u, v, weight))
#         print("Minimum Spanning Tree" , minimumCost)
 
# # Driver code
# g = Graph(4)
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)
 
# # Function call
# g.KruskalMST()
 


def find(graph,node): ##chercher tout les sommets dans la graphe
    if graph[node]<0: #cherche les noeuds construire les arcs  ont le cout minimal 
        #print(node)
        return node
    else:
        temp= find(graph,graph[node]) #cherche les noeuds 
        graph[node]= temp
        print(temp)
        return temp

def union(graph,a,b,answer):
    ta=a
    tb=b
    a= find(graph,a)
    b=find(graph,b)
    if a==b:
        pass
    else:
        answer.append([ta,tb])#ajout les arcs dans la list answer
        if graph[a]<graph[b]: #compare le rang de a et b
            graph[a]+=graph[b] 
            graph[b]=a #l'arc doit etre oriente de b vers a 
        else:
            graph[b]=graph[a]+graph[b]
            graph[a]=b
def __main__():           
    ipt=[[1,2,1],[1,3,3],[2,6,4],[3,6,2],[3,4,1],[4,5,5],[6,5,6],[7,5,7]]
    n=7
    answer=[] #initialiser list contient les arcs couvre la arbre minimal sans boucle
    ipt=sorted(ipt,key=lambda ipt:ipt[2]) # trie les arcs du graph a partir de cout (position 2 dans la liste) d'une façon croisant
    graph=[-1]*(n+1) # list initialiser -1
    for u,v,d in ipt: #parcour les elts du sommet voisin et le cout de la list ipt
        union(graph,u,v,answer)
    for item in answer:
        print(item)
    G = nx.DiGraph()
    G.add_edges_from([(1,2),(1,3),(2,6),(3,6),(3,4),(4,5),(6,5),(7,5)])
    val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}
    values = [val_map.get(node, 0.35) for node in G.nodes()]

    # Specify the edges you want here
    red_edges = [(1,2), (3,4),(3,6),(1,3),(4,5),(7,5)]
    edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    plt.show()

    
            
__main__()