
#Stupid wannabe shit dont work

from collections import deque
class Solution:
    def allPathsSourceTarget(self,graph):   #List[List[int]]
        if len(graph) >  0 and len(graph) < 20:
            destinationNode = len(graph ) - 1
            graph = self.buildGraph(graph)
            stack = deque()
            stack.append((0, [0]))
            res = []
            while len(stack) > 0:
                curr = stack.pop()
                currNode, currPath = curr[0], curr[1]
                if currNode == destinationNode:
                    res.append(currNode)
                else:
                    for neighbor in graph[currNode]:
                        newPath = currPath.copy()
                        newPath.append(neighbor)
                        stack.append((neighbor, newPath)) 
                return res
 
    def  buildGraph(self,edges):
        graph = {}
        # graph = defaultDict(set) # dont work
        for (node, neighbors) in enumerate(edges): 
            for neighbor  in neighbors:
                graph[node] = neighbor
                 
        return graph                        
         
def csFindAllPathsFromAToB(graph):
    if len(graph) >  0 and len(graph) < 100:
        csd = Solution()
        csd.allPathsSourceTarget(graph)
    return graph
   
   
   
   
   
   
from collections import deque   
# Driver code
from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self,graph):
        if len(graph) >  0 and len(graph) < 20:
            destinationNode = len(graph ) - 1
            graph = self.buildGraph(graph)
            stack = deque()
            stack.append((0, [0]))
            res = []
            while len(stack) > 0:
                curr = stack.pop()
                currNode, currPath = curr[0], curr[1]
                if currNode == destinationNode:
                    res.append(currNode)
                else:
                    for neighbor in graph[currNode]:
                        newPath = currPath.copy()
                        newPath.append(neighbor)
                        stack.append((neighbor, newPath)) 
                return res
 
    def  buildGraph(self,edges):
        # graph = {}
        graph = defaultdict(set) # dont work
        for (node, neighbors) in enumerate(edges): 
            for neighbor  in neighbors:
                graph[node].add(neighbor)
                 
        return graph              

# class Graph:
#     def __init__(self):
#         self.graph = {}
    
#     def __repr__(self):
#         return str(self.graph)
    
#     def addNode(self,value):
#         if value not in self.graph:
#             self.graph[value] = set()        
            
#     def removeNode(self,value):
#         if value in self.graph:
#             self.graph.pop(value)
#             for otherNode in self.graph:
#                 if value in self.graph[otherNode]:
#                     self.graph[otherNode].remove(value)
                    
#     def addEdge(self,fromNode,toNode):
#         self.graph[fromNode].add(toNode)
    
#     def removeEdge(self,fromNode,toNode):
#         self.graph[fromNode].remove(toNode)
        
#     def edgeExists(self,fromNode,toNode):
#         return toNode in self.graph[fromNode]
                    
                     
# # from collections import deque


# def depthFirstTrav(graph,startingNode):
#     stack = deque()
#     stack.append(startingNode)
#     visited = set()
#     while len(stack) > 0:
#         currNode = stack.pop()
#         if currNode not in visited:
#             visited.add(currNode)
#             print(currNode)
#             for neighbor in graph[currNode]:
#                 stack.append(neighbor)
                             
                             
                        
# def dfs(s,indeg0,adj):
#     # Append the node in path
#     # and set visited
#     path  = []
#     path.append(s)
#     visited[s] = True
  
#     # Path started with a node
#     # having in-degree 0 and
#     # current node has out-degree 0,
#     # print current path
#     if outdeg0[s] and indeg0[path[0]]:
#         print(*path)
  
#     # Recursive call to print all paths
#     for node in adj[s]:
#         if not visited[node]:
#             dfs(node)
  
#     # Remove node from path
#     # and set unvisited
#     path.pop()
#     visited[s] = False
  
  
# def print_all_paths(n,indeg0,adj):
#     for i in range(n):
  
#         # for each node with in-degree 0
#         # print all possible paths
#         if indeg0[i] and adj[i]:
#             path = []
#             visited = [False] * (n + 1)
#             dfs(i,indeg0,adj)
  

  

         
def csFindAllPathsFromAToB(graph):
    if len(graph) >  0 and len(graph) < 100:
        # n = 6
        # # set all nodes unvisited
        # visited = [False] * (n + 1)
        # path = []
        
        # # edges = (a, b): a -> b
        # edges = [(5, 0), (5, 2), (2, 3),
        #         (4, 0), (4, 1), (3, 1)]
        
        # # adjacency list for nodes
        # adj = defaultdict(list)
        
        # # indeg0 and outdeg0 arrays
        # indeg0 = [True]*n
        # outdeg0 = [True]*n
        
        # for edge in edges:
        #     u, v = edge[0], edge[1]
        #     # u -> v
        #     adj[u].append(v)
        
        #     # set indeg0[v] <- false
        #     indeg0[v] = False
        
        #     # set outdeg0[u] <- false
        #     outdeg0[u] = False
        
        # print('All possible paths:')
        # print_all_paths(n,indeg0,adj)

        # # csd = Solution()
        # # csd.allPathsSourceTarget(graph)
        # depthFirstTrav(graph,0)
        ccs = Solution()
        fs = ccs.allPathsSourceTarget(graph)
        return graph
   
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
