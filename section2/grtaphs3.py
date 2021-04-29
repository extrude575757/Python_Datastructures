   
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
        graph = defaultdict(set) 
        for (node, neighbors) in enumerate(edges): 
            for neighbor  in neighbors:
                graph[node].add(neighbor)
                 
        return graph              

def csFriendCircles(M):
    if len(M) > 0 and len(M) < 3:
        ss = Solution()
        ff = deque()
        # ff.append((0, [0]))
        ff = ss.allPathsSourceTarget(M)
        return ff





