#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
    
#   def retn(self):
#       return self.value
# wONT work wont allow me to traverse threw wont traverse threw t recursion is the only way maybe. There is no itterative approach for this

# from collections import deque
# class Sol:
    
#     def maxDepth(self,root):
#         if root == None:
#             return 0
#         self.maxDepth = 0
#         self.maxDepthHelper(root,1)
#         return self.maxDepth
    
    
#     def maxDepthHelper(self,root,currDepth):
#         # base-case
#         if root.left == None and root.right == None:
#             if currDepth > self.maxDepth:
#                 self.maxDepth = currDepth
#             return 
#         # recursive-cases
#         if root.left != None:
#             self.maxDepthHelper(root.left, currDepth + 1)
#         if root.right  != None:
#             self.maxDepthHelper(root.right, currDepth + 1)
    
#     def iterativeMaxDepth(self,root):
#         if root == None:
#             return 0
#         stack = deque()
#         stack.append((root,1))
#         maxDepthFound = 1
#         while len(stack) > 0:
#             curr = stack.popleft()
#             currNode, currDepth = curr[0], curr[1]
#             if currDepth   > maxDepthFound:
#                 maxDepthFound = currDepth
#             if currNode.left != None:
#                 stack.append((currNode.left, currDepth  + 1))
#             if currNode.right != None:
#                 stack.append((currNode.right, currDepth + 1))
#         return  maxDepthFound

# class Solution:
    
#     # def kthSmallest(self,root,k):
#     #     res = []
#     #     self.kthSmallestHelper(root,k,res)
#     #     return res[k - 1]
    
#     # def kthSmallestHelper(self,root,k,res):
#     #     if root.left  != None:
#     #        self.kthSmallestHelper(root.left,k,res)
#     #     res.append(root.value)
#     #     #recursive case 2
#     #     if root.right != None:
#     #         self.kthSmallestHelper(root.right,k,res)
    
#     def kthSmallest(self,root,k):
#         self.value = 0
#         return self.kthSmallestHelper(root,k)
        
#     def kthSmallestHelper(self,root,k):
#         #recurive case 1
#         if root.left != None:
#             leftSubtree = self.kthSmallestHelper(root.left,k)
#             if leftSubtree != None:
#                 return leftSubtree
#         self.value += 1
#         # base-case 
#         if self.value == k:
#             return root.val
            
#         if root.right != None:
#             rightSubtree = self.kthSmallestHelper(root.right,k)
#             if rightSubtree  != None:
#                 return rightSubtree
                
#         return None
        
        
        
        
        
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Recursive function to find the minimum depth of a path starting
# from the given node in a binary tree
def findMinDepth(root):
 
    # base case
    if root is None:
        return 0
 
    # find the minimum depth of the left subtree
    l = findMinDepth(root.left)
 
    # find the minimum depth of the right subtree
    r = findMinDepth(root.right)
 
    # if the left child does not exist, consider the depth
    # returned by the right subtree
    if root.left is None:
        return 1 + r
 
    # if the right child does not exist, consider the depth
    # returned by the left subtree
    if root.right is None:
        return 1 + l
 
    # otherwise, choose the minimum depth returned by the
    # left and right subtree
    return min(l, r) + 1
 
 
# if __name__ == '__main__':
 
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.left = Node(6)
#     root.right.right = Node(7)
#     root.left.left.right = Node(8)
#     root.left.right.right = Node(9)
#     root.right.right.left = Node(10)
#     root.right.right.left = Node(11)
#     root.left.left.right.right = Node(12)
 
    # print("The minimum depth is", findMinDepth(root))


def treeSize(root):
        return findMinDepth(root)

def inOrder(root):
   dpth = 0
   size = treeSize(root)
   outit = []
   if size > 1:
       while size > dpth:
           dpth = dpth +  1
           if dpth == 1:
               outit.append(root.value)
           if root.left != None and dpth > 1:
            #    root.left
               outit.append(root.left.value)
           if root.right != None and dpth > 1:
               outit.append(root.right.value)
        #    if root.right.left != None and dpth > 2:
        #        outit.append(root.right.left.value)
        #    else:
        #        pass
        #    if root.right.right != None and dpth > 2:
        #        outit.append(root.right.right.value)
           if root.left.right != None and dpth > 2:
            #    root.left
               outit.append(root.left.right.value)
           if root.left.left != None and dpth > 2:
               outit.append(root.left.left.value)
           
       return outit
   elif size == 1:
       return root.value
   else:
       return 0
#    if root:
#        inOrder(root.left)
#        print (root.value)
#        inOrder(root.right)
    #    print(root.value)


def traverseTree(root):
    # ssd = 0
    # # fd = t.keys()
    # # ssd = t.value
    # ss =  Sol()
    # sl = Solution()

    # # ll  = sl.kthSmallestHelper(root)
    # fly = ss.iterativeMaxDepth(root)
    # if fly > 1:
    #         ll = sl.kthSmallestHelper(root,fly-1)
    # return fly
    
    
    
    return inOrder(root)








def dfs_non_recursive(graph, source):

       if source is None or source not in graph:

           return "Invalid input"

       path = []

       stack = [source]

       while(len(stack) != 0):

           s = stack.pop()

           if s not in path:

               path.append(s)

           if s not in graph:

               #leaf node
               continue

           for neighbor in graph[s]:

               stack.append(neighbor)

       return " ".join(path)
       
       
       
       
 
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Iterative function for inorder tree traversal
def inOrder(root):
     
    # Set current to root of binary tree
    current = root
    stack = [] # initialize stack
    done = 0
     
    while True:
         
        # Reach the left most Node of the current Node
        if current is not None:
             
            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)
         
            current = current.left
 
         
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif(stack):
            current = stack.pop()
            print(current.value, end=" ") # Python 3 printing
         
            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right
 
        else:
            break
      
    print()
 
# Driver program to test above function
       
       
       
       


