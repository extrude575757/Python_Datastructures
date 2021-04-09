
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
