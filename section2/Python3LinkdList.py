

def buyAndSellStock(stock_price):
    max_profit_val, current_max_val = 0, 0 
    for price in reversed(stock_price):                       
        current_max_val = max(current_max_val, price)          
        potential_profit = current_max_val - price          
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val

# print(buy_and_sell([8, 10, 7, 5, 7, 15]))
# print(buy_and_sell([1, 2, 8, 1]))
# print(buy_and_sell([]))


#Buy on the best day to make the most profits

def buyAndSellStock(prices):
    
    mostProfit = 0
    profits = []
    i = 0
    pp = len(prices)  - 1
    for ii in prices: 

        xx = i + 1
        for x in prices:
            
            if xx < pp:
                if (ii < x and xx > i):
                    isitProfitable =  x -ii
                    profits.append(isitProfitable)
        xx = xx + 1
            
    i = i + 1
    
    
    if profits == []:
        return 0
    elif len(profits) <= 1:
        return 0
    for prof in profits: 
        if mostProfit <= prof: 
            mostProfit = prof
    return mostProfit
        
        
        
## Node list Nmber s

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

#Singly-linked lists are already defined with this interface:
class ListNode:
  def __init__(self, x):
    self.value = x
    self.next = None
  def __repr__(self):
      return f"Node{self.value}" 
#   def getD():

def insertValueIntoSortedLinkedList(l, value):
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    ss = ''
    ss = b.next
    print(a.next,ss)
    return 1
    
    
    # Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

#Singly-linked lists are already defined with this interface:
class ListNode:
  def __init__(self, x):
    self.value = x
    self.next = None
  def __repr__(self):
      return f"Node({self.value})" 
#   def getD():

def insertValueIntoSortedLinkedList(l, value):
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    ss = ''
    ss = b.next
    print(a.next,ss)
    return 1
    
    
    
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

#Singly-linked lists are already defined with this interface:Traverse them
# Head is the first node you are traversing from 
class ListNode:
  def __init__(self, x):
    self.value = x
    self.next = None
  def __repr__(self):
      return f"Node({self.value})" 
#   def getD():

    
def traverseLinkedList(startingNode):
      curr = startingNode
      while curr != None: 
          print(curr)
          curr = curr.next
    
        
def insertValueIntoSortedLinkedList(l, value):
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    ss = 0
    ss = b.next
    
    traverseLinkedList(a)
    # print(a.next,ss)
    return 1
    
    
    
    
    
    # Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

#Singly-linked lists are already defined with this interface:
class ListNode:
  def __init__(self,l, x):
    self.value = x
    # self.ll = []
    # llm  = list(l)
    self.ll = []
    self.inc = 0
    while len(self.ll) < self.inc:
        self.ll.insert(l[self.inc])
        self.inc = self.inc + 1
        self.next = None
#   def __repr__(self):
#       return f"Node({self.value})" 
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
    a = ListNode(l,value)
    b = ListNode(l,value)
    c = ListNode(l,value)
    a.next = b
    b.next = c
    ss = []
    ss = b.ll
    
    traverseLinkedList(a,value)
    if len(a.ll) > 0:
     for iz in a.next.ll:
         print('iz')
    # print(a.next,ss)
    if len(a.ll) > 0:
        return a.ll
