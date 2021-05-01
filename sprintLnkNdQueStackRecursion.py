







# # Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#     self.head = None
    
  
  
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
    self.head = None
    
  def printList(self):
        temp = self.head
        snapit = []
        c= 0
        while (temp):
            # print(temp.value)
            snapit.append(temp.value)
            temp = temp.next
            c = c + 1
        return snapit

# Node class
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
  
  
    # Functio to insert a new node at the beginning
    def push(self, new_data):
  
        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)
  
        # 3. Make next of new Node as head
        new_node.next = self.head
  
        # 4. Move the head to point to new Node
        self.head = new_node
  
  
    # This function is in LinkedList class. Inserts a
    # new node after the given prev_node. This method is
    # defined inside LinkedList class shown above */
    def insertAfter(self, prev_node, new_data):
  
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
  
        #  2. create new node &
        #      Put in the data
        new_node = Node(new_data)
  
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
  
        # 5. make next of prev_node as new_node
        prev_node.next = new_node
  
  
    # This function is defined in Linked List class
    # Appends a new node at the end.  This method is
    # defined inside LinkedList class shown above */
    def append(self, new_data):
  
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
  
        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return
  
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
  
        # 6. Change the next of last node
        last.next =  new_node
  
  
    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        snapit = []
        c= 0
        while (temp):
            print(temp.data)
            snapit.append(temp.data)
            temp = temp.next
            c = c + 1
        return snapit
        
def reverseLinkedList(l):
    
    ll = ListNode(l)
    l2 = ListNode(l)
    ll.head = l
    l2.head = l
    eq = []
    eq = ll.printList()
    eqld = []
    for iia in eq[::-1]:
        eqld.append(iia)
    return eqld
