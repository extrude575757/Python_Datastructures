# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

#Singly-linked lists are already defined with this interface:
class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
  


class ListNode:
  def __init__(self, x):
    self.value = x
    self.next = None
    # self.ll = []
    # llm  = list(l)
    self.ll = []
    # self.inc = 0
    # while len(self.ll) < self.inc:
    #     self.ll.insert(l[self.inc])
    #     self.inc = self.inc + 1
    #     self.next = None
#   def __repr__(self):
#       return f"Node({self.value})" 
  def push(self, val):
    self.ll.append(val)
  def getD(self):
    return self.ll
 

    
def traverseLinkedList(startingNode,value):
    w = []
    w = startingNode
    curr = w
    
    #   print(startingNode.next.ll)
    #   while curr.next != None: 
          
    #     #   for i in startingNode.getD:
    #     #       print(i)
    #     #   for iz in startingNode.ll:
    #     #       print(iz)
    #       print (curr.getD)
    #     #   for iz in curr.ll:
    #     #       print(iz)
    #       curr = curr.next
    while startingNode.next != None:
        for imc in startingNode.next.ll:
            print(imc)
    
        
def insertValueIntoSortedLinkedList(l, value):
    # a = ListNode(value)
    # b = ListNode(value)
    # c = ListNode(value)
    # a.next = b
    # b.next = c
    # for fsd in l:
    #     a.push(fsd)
    
    
    # ss = []
    # ss = b.ll
    
    # traverseLinkedList(a,value)
    # if len(a.ll) > 0:
    #  for iz in a.next.ll:
    #      print('iz')
    # # print(a.next,ss)
    # if len(a.ll) > 0:
    #     return a.ll
    # Code execution starts here
    # if __name__=='__main__':
  
        # Start with the empty list
        llist = LinkedList()
    
        llist.head = Node([1])
        second = Node([2])
        third = Node([3,23,6])
    
        

        llist.head.next = second; # Link first node with second 
    

    
        second.next = third; # Link second node with the third nodeq
    
        print(third.data)
        return l
        
        

