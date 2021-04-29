"""
Traversing trees
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

Example:
Input: [2,None,3,4]

   2
    \
     3
    /
   4
Output: [2,4,3]

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] array.integer

[Python 3] Syntax Tips

"""



# #
# # Binary trees are already defined with this interface:
# class Tree(object):
#     def __init__(self, x):
#         self.value = x
#         self.left = None
#         self.right = None

#     # Insert Node
#     def insert(self, data):

#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

#     # Print the Tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()

#     # Inorder traversal
#     # Left -> Root -> Right
def inorderTraversal(root):
        res = []
        if root:
            res = inorderTraversal(root.left)
            res.append(root.value)
            res = res + inorderTraversal(root.right)
        return res
        
def binaryTreeInOrderTraversal(root):
    fd = []
    
    fd =  inorderTraversal(root)
    return fd
        # print(root)
        # res = []
        # if root:
        #     res = self.inorderTraversal(root.left)
        #     res.append(root.value)
        #     res = res + inorderTraversal(root.right)
        # return res

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

An array that contains the values at t's nodes, ordered as described above.

[Python 3] Syntax Tips

"""


#REFUSES TO WORK
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
    
#   def retn(self):
#       return self.value
def traverseTree(t):
    ssd = 0
    # fd = t.keys()
    # ssd = t.value
    for i in t.value:
        for key,value in i.items():
         print(key,value)
    return ssd






#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

'''
You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf node. As a reminder, a leaf node is a node with no children.

Example:
Given the binary tree [5,7,22,None,None,17,9],

    5
   / \
  7  22
    /  \
   17   9
your function should return its minimum depth = 2.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] integer

[Python 3] Syntax Tips

'''



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




def minimumDepthBinaryTree(root):
        return findMinDepth(root)






