
'''
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

Example

For

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 10,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": -3,
        "left": null,
        "right": null
    }
}
the output should be
treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

The given tree looks like this:

    5
   / \
  2  -3
 / \
10  4
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 710,
-1000 ≤ node value ≤ 1000.

[output] array.string

The root-to-leaf paths, sorted by the leaves in the order that they appear in the pre-order traversal (i.e. from the leftmost leaf to the rightmost).
'''

#
# Binary trees are already defined with this interface:
class Flip(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
    
    
    def __getitem__(self, key):
        found = []
        if range(self.value) >= 0:
            for mapping in self.value:
                if mapping.get(key):
                    found.append(mapping.get(key))
                else:
                    continue
        return found

    def get(self, key):
        return self.__getitem__(key)
    def prnt(self):
        return self.value
    
    def findObjectByName(self, name):
        if self.value == name:
            return self
        else:
            for child in self.children:
                match = child.findObjectByName(name)
                if match:
                    return match
                    
                    
# A binary tree node
class Dontwork:
  
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
  
    # Computes the number of nodes in tree
    def size(node):
        if node is None:
            return 0 
        else:
            return (size(node.left)+ 1 + size(node.right))
  
  
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
    return max(l, r) + 1


# class Node:
#     # constructor to create tree node
#     def __init__(self, data):
#         self.value = data
#         self.left = None
#         self.right = None
  
# function to print all path from root
# to leaf in binary tree
def printPaths(root):
    # list to store path 
    # Try with a stack deque
    path = []
    path.append(printPathsRec(root, path, 0))
    return path
# Helper function to print path from root 
# to leaf in binary tree
def printPathsRec(root, path, pathLen):
      
    # Base condition - if binary tree is
    # empty return
    if root is None:
        return []
  
    # add current root's data into 
    # path_ar list
      
    # if length of list is gre
    if(len(path) > pathLen): 
        path[pathLen] = root.value
    else:
        path.append(root.value)
  
    # increment pathLen by 1
    pathLen = pathLen + 1
  
    if root.left is None and root.right is None:
          
        # leaf node then print the list
        return printArray(path, pathLen)
        
    else:
        # try for left and right subtree
        printPathsRec(root.left, path, pathLen)
        printPathsRec(root.right, path, pathLen)
        # return printArray(path,pathLen)
  
# Helper function to print list in which 
# root-to-leaf path is stored
def printArray(ints, len):
    rere = ""
    faster = []
    res = []
    for i in ints[0 : len]:
        # print(i," ",end="")
        fs = "->"
        ff = str(i)+fs
        rere= rere + ff
    ros = ''
    faster.append(rere)
    for i in faster:
        ros = ros + i
    # print(ros)
    res.append(ros)
    print(res)
    return res
  
# # Driver program to test above function
# """
# Constructed binary tree is 
#             10
#         / \
#         8     2
#     / \ /
#     3 5 2
# """
# root = Node(10)
# root.left = Node(8)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(5)
# root.right.left = Node(2)
# printPaths(root)
        
def treePaths(t):
    return  printPaths(t)






'''
Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
the output should be
traverseTree(t) = [1, 2, 4, 3, 5].

This t looks like this:

     1
   /   \
  2     4
   \   /
    3 5
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

Guaranteed constraints:
0 ≤ tree size ≤ 104.

[output] array.integer

An array that contains the values at t's nodes, ordered as described above.

[Python 3] Syntax Tips
'''



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
           if root.left != None and dpth == 1:
            #    root.left
               outit.append(root.left.value)
           if root.right != None and dpth == 1:
               outit.append(root.right.value)
        #    if root.right.left != None and dpth > 2:
        #        outit.append(root.right.left.value)
        #    else:
        #        pass
        #    if root.right.right != None and dpth > 2:
        #        outit.append(root.right.right.value)
           if root.left.right != None and dpth == 2:
            #    root.left
               outit.append(root.left.right.value)
           if root.left.left != None and dpth == 2:
               outit.append(root.left.left.value)
               
        #    if root.left.right != None and dpth > 2:
        #     #    root.left
        #        outit.append(root.left.right.value)
           if root.right != None and dpth > 2:
               outit.append(root.right.left.value)
           
       return outit
   elif size == 1:
       return root.value
   else:
       return []
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

from collections import deque
class Sol:
    
    def maxDepth(self,root):
        if root == None:
            return 0
        self.maxDepth = 0
        self.maxDepthHelper(root,1)
        return self.maxDepth
    
    
    def maxDepthHelper(self,root,currDepth):
        # base-case
        if root.left == None and root.right == None:
            if currDepth > self.maxDepth:
                self.maxDepth = currDepth
            return 
        # recursive-cases
        if root.left != None:
            self.maxDepthHelper(root.left, currDepth + 1)
        if root.right  != None:
            self.maxDepthHelper(root.right, currDepth + 1)
    
    def iterativeMaxDepth(self,root):
        if root == None:
            return 0
        stack = deque()
        stack.append((root,1))
        maxDepthFound = 1
        while len(stack) > 0:
            curr = stack.popleft()
            currNode, currDepth = curr[0], curr[1]
            if currDepth   > maxDepthFound:
                maxDepthFound = currDepth
            if currNode.left != None:
                stack.append((currNode.left, currDepth  + 1))
            if currNode.right != None:
                stack.append((currNode.right, currDepth + 1))
        return  maxDepthFound

class Solution:
    
    # def kthSmallest(self,root,k):
    #     res = []
    #     self.kthSmallestHelper(root,k,res)
    #     return res[k - 1]
    
    # def kthSmallestHelper(self,root,k,res):
    #     if root.left  != None:
    #        self.kthSmallestHelper(root.left,k,res)
    #     res.append(root.value)
    #     #recursive case 2
    #     if root.right != None:
    #         self.kthSmallestHelper(root.right,k,res)
    
    def kthSmallest(self,root,k):
        self.value = 0
        return self.kthSmallestHelper(root,k)
        
    def kthSmallestHelper(self,root,k):
        #recurive case 1
        if root.left != None:
            leftSubtree = self.kthSmallestHelper(root.left,k)
            if leftSubtree != None:
                return leftSubtree
        self.value += 1
        # base-case 
        if self.value == k:
            return root.val
            
        if root.right != None:
            rightSubtree = self.kthSmallestHelper(root.right,k)
            if rightSubtree  != None:
                return rightSubtree
                
        return None
        
def traverseTree(root):
    ssd = 0
    # fd = t.keys()
    # ssd = t.value
    ss =  Sol()
    sl = Solution()

    # ll  = sl.kthSmallestHelper(root)
    fly = ss.iterativeMaxDepth(root)
    if fly > 1:
            ll = sl.kthSmallestHelper(root,1)
    return fly

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

from collections import deque
class Sol:
    
    def maxDepth(self,root):
        if root == None:
            return 0
        self.maxDepth = 0
        self.maxDepthHelper(root,1)
        return self.maxDepth
    
    
    def maxDepthHelper(self,root,currDepth):
        # base-case
        if root.left == None and root.right == None:
            if currDepth > self.maxDepth:
                self.maxDepth = currDepth
            return 
        # recursive-cases
        if root.left != None:
            self.maxDepthHelper(root.left, currDepth + 1)
        if root.right  != None:
            self.maxDepthHelper(root.right, currDepth + 1)
    
    def iterativeMaxDepth(self,root):
        if root == None:
            return 0
        stack = deque()
        stack.append((root,1))
        maxDepthFound = 1
        while len(stack) > 0:
            curr = stack.popleft()
            currNode, currDepth = curr[0], curr[1]
            if currDepth   > maxDepthFound:
                maxDepthFound = currDepth
            if currNode.left != None:
                stack.append((currNode.left, currDepth  + 1))
            if currNode.right != None:
                stack.append((currNode.right, currDepth + 1))
        return  maxDepthFound

class Solution:
    
    # def kthSmallest(self,root,k):
    #     res = []
    #     self.kthSmallestHelper(root,k,res)
    #     return res[k - 1]
    
    # def kthSmallestHelper(self,root,k,res):
    #     if root.left  != None:
    #        self.kthSmallestHelper(root.left,k,res)
    #     res.append(root.value)
    #     #recursive case 2
    #     if root.right != None:
    #         self.kthSmallestHelper(root.right,k,res)
    
    def kthSmallest(self,root,k):
        self.curr = 0
        return self.kthSmallestHelper(root,k)
        
    def kthSmallestHelper(self,root,k):
        #recurive case 1
        if root.left != None:
            leftSubtree = self.kthSmallestHelper(root.left,k)
            if leftSubtree != None:
                return leftSubtree
        self.curr += 1
        # base-case 
        if self.curr == k:
            return root.val
            
        if root.right != None:
            rightSubtree = self.kthSmallestHelper(root.right,k)
            if rightSubtree  != None:
                return rightSubtree
                
        return None
        
def traverseTree(root):
    ssd = 0
    # fd = t.keys()
    # ssd = t.value
    ss =  Sol()
    sl = Solution()
    # ll  = sl.kthSmallestHelper(root)
    fly = ss.iterativeMaxDepth(root)
    return fly

class Solution:
    
    def kthSmallest(self,root,k):
        self.curr = 0
    
    def kthSmallestHelper(self,root,k):
        if root.left  != None:
            leftSubtree = self.kthSmallestHelper(root.left,k)
            if leftSubtree != None:
                return leftSubtree
        self.curr  += 1
        if self.curr  == k:
            return root.val
        if  root.right != None:
            rightSubtree  = self.kthSmallestHelper(root.right,k)
            if rightSubtree != None:
                return rightSubtree
        return None
        
        
        
        class Solution:
    
    def kthSmallest(self,root,k):
        res = []
        self.kthSmallestHelper(root,k,res)
        return res[k - 1]
    
    def kthSmallestHelper(self,root,k,res):
        if root.left  != None:
           self.kthSmallestHelper(root.left,k,res)
        res.append(root.value)
        #recursive case 2
        if root.right != None:
            self.kthSmallestHelper(root.right,k,res)

# Sizes of bt the max depths
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
    
#   def retn(self):
#       return self.value
# wONT work wont allow me to traverse threw wont traverse threw t recursion is the only way maybe. There is no itterative approach for this

from collections import deque
class Sol:
    
    def maxDepth(self,root):
        if root == None:
            return 0
        self.maxDepth = 0
        self.maxDepthHelper(root,1)
        return self.maxDepth
    
    
    def maxDepthHelper(self,root,currDepth):
        # base-case
        if root.left == None and root.right == None:
            if currDepth > self.maxDepth:
                self.maxDepth = currDepth
            return 
        # recursive-cases
        if root.left != None:
            self.maxDepthHelper(root.left, currDepth + 1)
        if root.right  != None:
            self.maxDepthHelper(root.right, currDepth + 1)
    
    def iterativeMaxDepth(self,root):
        if root == None:
            return 0
        stack = deque()
        stack.append((root,1))
        maxDepthFound = 1
        while len(stack) > 0:
            curr = stack.popleft()
            currNode, currDepth = curr[0], curr[1]
            if currDepth   > maxDepthFound:
                maxDepthFound = currDepth
            if currNode.left != None:
                stack.append((currNode.left, currDepth  + 1))
            if currNode.right != None:
                stack.append((currNode.right, currDepth + 1))
        return  maxDepthFound

    

def traverseTree(root):
    ssd = 0
    # fd = t.keys()
    # ssd = t.value
    ss =  Sol()
    fly = ss.iterativeMaxDepth(root)
    return fly



"""
Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
the output should be
traverseTree(t) = [1, 2, 4, 3, 5].

This t looks like this:

     1
   /   \
  2     4
   \   /
    3 5
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

Guaranteed constraints:
0 ≤ tree size ≤ 104.

[output] array.integer
9880
An array that contains the values at t's nodes, ordered as described above.
"""






'''
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] boolean

[Python 3] Syntax Tips
'''



#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
  
# function to find height of binary tree
def height(root):
      
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
  
# function to check if tree is height-balanced or not
def isBalanced(root):
      
    # Base condition
    if root is None:
        return True
  
    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)
  
    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and isBalanced(
    root.left) is True and isBalanced( root.right) is True:
        return True
  
    # if we reach here means tree is not 
    # height-balanced tree
    return False
  
# # Driver function to test the above function

def balancedBinaryTree(root):

    # r = Tree(root) 
    if isBalanced(root):
        print("Tree is balanced")
        return True
    else:
        print("Tree is not balanced")
        return False
