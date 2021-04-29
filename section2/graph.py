










class Graph:
    def __init__(self):
        self.graph = {}
    
    def __repr__(self):
        return str(self.graph)
    
    def addNode(self,value):
        if value not in self.graph:
            self.graph[value] = set()        
            
    def removeNode(self,value):
        if value in self.graph:
            self.graph.pop(value)
            for otherNode in self.graph:
                if value in self.graph[otherNode]:
                    self.graph[otherNode].remove(value)
                    
    def addEdge(self,fromNode,toNode):
        self.graph[fromNode].add(toNode)
    
    def removeEdge(self,fromNode,toNode):
        self.graph[fromNode].remove(toNode)
        
    def edgeExists(self,fromNode,toNode):
        return toNode in self.graph[fromNode]
                    
                    
                    
                    





from collections import deque


def depthFirstTrav(graph,startingNode):
    stack = deque()
    stack.append(startingNode)
    visited = set()
    while len(stack) > 0:
        currNode = stack.pop()
        if currNode not in visited:
            visited.add(currNode)
            print(currNode)
            for neighbor in graph[currNode]:
                stack.append(neighbor)
                   
    
    
myGraph = Graph()
myGraph.addNode(1)
myGraph.addNode(4)
myGraph.addNode(3)
myGraph.addNode(15)
myGraph.addEdge(1,4)
myGraph.addEdge(4,15)
myGraph.edgeExists(15,4)
#myGraph.removeNode(3)
print(myGraph)




adjList = {1: {2,3}, 2: {4,8}, 3: {}}
depthFirstTrav(adjList,1)
