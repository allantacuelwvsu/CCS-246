import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

num_nodes = 10
edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (2, 7),
         (3, 7), (3, 8), (4, 9), (5, 6), (7, 10), (9, 10)]

class Graph: #class nga gahimo kang adjacency list graph contains functions...
    def __init__(self, num_nodes, edges): #tana ja ang constructor
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes + 1)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        self.data.pop(0) #pop ko kay di kaya isipon kang range and num_nodes kay ga array counting sha ya (from 0) te i +1 ko. te tapos maappend ako don, mahimo paths, gahimo sha blank nga path sa una as result kang pag +1 sa range so kinanglan i-pop otherwise detrimental tana sasequences karon.
        #example, may num_nodes ako nga 10, mahimo ran nga 0 to 9 pero i + 1 ko para mahimo nga 0-10 tapos i pop(0) ko para i delete ang zero para mahimo nga 1-10 ezpz
    
    def __repr__(self): #function nga ginarewrite and data into dictionary syntax or adjacency list
        return"\n".join(["{}: {}".format(n+1, neighbors) for n, neighbors in enumerate(self.data)])
    
    def __str__(self): #function nga ginatawag ang __repr__ automatically
        return self.__repr__()
    
    def get_adjacency_list(self):
        adjacency_list = {}
        for n, neighbors in enumerate(self.data):
            adjacency_list[n + 1] = neighbors
        return adjacency_list

g1 = Graph(num_nodes, edges)
graph = g1.get_adjacency_list() #reassign contents kang g1 into graph dictionary
print("g1.data Adjacency List:\n(Node: [Neighbor Node, Neighbor Node, ...])")
print(g1)
print("\n")
print("graph Adjacency List: \n(Node: [Neighbor Node, Neighbor Node, ...])")
print(graph)
print("\n") #ambalon nyo lamang lamang napangubra ko ja ang graph ja amo run ja ang tree graph, lantawa nyo tsura na sa jupiter notebook. amoja kaja itsura kang tree graph kung i convert tana sa code(dictionary)

BFS_Start = 10
BFS_Target = 5

def BFS(graph, BFS_Start, BFS_Target):
    global BFSPath #extract ang BFSPath para magamit outside kang bfs function
    visited = set()
    queue = deque([(BFS_Start, [BFS_Start])])

    while queue:
        node, path = queue.popleft()
        if node == BFS_Target:
            print("Shortest path:", ' -> '.join(map(str, path)))
            BFSPath = [path]
            return path
        if node not in visited:
            visited.add(node)
            for child in graph.get(node, []):
                if child not in visited:
                    new_path = path + [child]
                    queue.append((child, new_path))

BFS(graph, BFS_Start, BFS_Target)
print("\n")
print(BFSPath)