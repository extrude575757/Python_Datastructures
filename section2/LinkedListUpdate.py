# A complete working Python program to demonstrate all
# insertion methods of linked list
  
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
  
  
  
 
        
def travLink(startingNode):
        curr = startingNode
        while curr != None:
            # for char in curr.value:
            #     print(char)
                    
                curr = curr.next
        
def insertValueIntoSortedLinkedList(l, value):
        bc = [3,55,22,342,12,55]
        # bc = l
        a = LinkedList()
        a.push(l)
        # a.printList()
        # print(l)
        return a.printList()

"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[output] linkedlist.integer

A list that contains elements from both l1 and l2, sorted in non-decreasing order.
"""

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


def mergeTwoLinkedLists(l1, l2):
    a = ListNode(l1)
    b = ListNode(l2)
    a.head = l1
    b.head = l2
    a.next = b.head
    # a.next = l2
    aa = []
    aa = a.printList()
    bb = []
    bb = b.printList()
    b.printList()
    lens = len(bb) + len(aa)
    cc = 0
    con = []
    if bb == [] and aa == []:
        return con
    else:
        for ii in aa:
            con.append(ii)
            
        for ii in bb:
            con.append(ii)
    
    concon = sorted(con)
    
    return concon



