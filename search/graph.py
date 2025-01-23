import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        fakeq = [] #my "queue" is a list because I feel like using the queue package
        visited = []
        myparent = {} #figure out how to store answer

        G = self.graph

        if start not in G.nodes:
            raise ValueError("The input start node is not in the graph")  ##raises an exception
        
        if (end is not None) and (end not in G.nodes):
            raise ValueError("The input end node is not the graph")
        
        if not set(list(G.nodes)):
            raise ValueError("The input graph is empty and contains no nodes")
        
        fakeq.append(start)
        visited.append(start)
        
        while len(fakeq) != 0:
            v = fakeq[0]
            N = G.adj[v]
            fakeq = fakeq[1:] #will just take the first item off the list i.e. pop off

            for neighbor in list(N):

                ## check if the list of adjacent things is empty (means it is disconnected)
                ##make sure it will quit if disconnected

                if neighbor not in set(visited):
                    myparent[neighbor] = v
                    visited.append(neighbor)
                    fakeq.append(neighbor) #add element to the back of the list i.e. push

                    if (end is not None) and (neighbor == end):
                        mypath = []
                        current = neighbor
                        while current != start:
                            mypath.insert(0, current)
                            current = myparent[current]
                        mypath.insert(0, start)
                        return mypath

                    else:
                        continue
            
        if end is not None:
            return None

        return visited




