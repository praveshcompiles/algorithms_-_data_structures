""" 
A Python program to demonstrate the adjacency 
list representation of the graph 
"""
  

class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
  
# A class to represent a graph
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 


# BFS of a Graph
class Graph: 
  
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        queue = [] 
  
 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s.
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True



# DFS of a Graph (from all the vertices)
class Graph: 
  
    # Constructor 
    def __init__(self): 
        self.graph = defaultdict(list) 
  

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def DFSUtil(self, v, visited): 
  
        visited[v]= True
        print v, 
  
        # Recur for all the vertices adjacent to 
        # this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
    # The function to do DFS traversal.
    def DFS(self): 
        V = len(self.graph)  #total vertices 
  
        # Mark all the vertices as not visited 
        visited =[False]*(V) 
  
        # DFS traversal starting from all vertices one 
        # by one 
        for i in range(V): 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 


# Program to detect cycle in an undirected graph
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = defaultdict(list) 
  
   
    def addEdge(self,v,w): 
        self.graph[v].append(w) 
        self.graph[w].append(v)
   
    def isCyclicUtil(self,v,visited,parent): 
  
        #Mark the current node as visited  
        visited[v]= True
   
        for i in self.graph[v]: 
            if  visited[i]==False :  
                if(self.isCyclicUtil(i,visited,v)): 
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif  parent!=i: 
                return True
          
        return False
           
   
    #Returns true if the graph contains a cycle, else false. 
    def isCyclic(self): 
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 

        for i in range(self.V): 
            if visited[i] ==False: #Don't recur for u if it is already visited 
                if(self.isCyclicUtil(i,visited,-1))== True: 
                    return True
          
        return False


# Program to count number of islands in a boolean 2D matrix 
class Graph: 
  
    def __init__(self, row, col, g): 
        self.ROW = row 
        self.COL = col 
        self.graph = g 
  

    def isSafe(self, i, j, visited): 
 
        return (i >= 0 and i < self.ROW and 
                j >= 0 and j < self.COL and 
                not visited[i][j] and self.graph[i][j]) 
              
  
    def DFS(self, i, j, visited): 
  
        # row and column numbers of 8 neighbours  
        # of a given cell 
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]; 
            colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]; 
          
        visited[i][j] = True
  
        # Recur for all connected neighbours 
        for k in range(8): 
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited): 
                self.DFS(i + rowNbr[k], j + colNbr[k], visited) 
  
  
    def countIslands(self): 
        # Initially all cells are unvisited 
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)] 
  
        count = 0
        for i in range(self.ROW): 
            for j in range(self.COL): 
                # If a cell with value 1 is not visited yet,  
                # then new island found 
                if visited[i][j] == False and self.graph[i][j] ==1: 
                    # Visit all cells in this island  
                    # and increment island count 
                    self.DFS(i, j, visited) 
                    count += 1
  
        return count 
  
  
graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 
  
  
row = len(graph) 
col = len(graph[0]) 
  
g= Graph(row, col, graph) 
  
print(g.countIslands())