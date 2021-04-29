"""
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2
Example 2:

Input: [1,2,1,2,1,2,80]
Output: 80
Note: You should be able to develop a solution that has O(n) time complexity.

[execution time limit] 4 seconds (py3)

[input] array.integer nums


"""
def getSingle(arr, n):
    ones = 0
    twos = 0
     
    for i in range(n):
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise OR
        twos = twos | (ones & arr[i])
         
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise OR
        ones = ones ^ arr[i]
         
        # The common bits are those bits
        # which appear third time. So these
        # bits should not be there in both
        # 'ones' and 'twos'. common_bit_mask
        # contains all these bits as 0, so
        # that the bits can be removed from
        # 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)
         
        # Remove common bits (the bits that
        # appear third time) from 'ones'
        ones &= common_bit_mask
         
        # Remove common bits (the bits that
        # appear third time) from 'twos'
        twos &= common_bit_mask
    return ones
     
    # # driver code
    # arr = [3, 3, 2, 3]
    # n = len(arr)
    


def csFindTheSingleNumber(nums):

    ll = len(nums)
    st = getSingle(nums,ll)
    
    return st
    
    
    
    
    
    
    
    
"""    
Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.
"""



class Node:
    def __init__(self, data, nextt=None, head=None):
        self.data = data
        self.next = nextt
        self.head = head
def Nmaxelements(list1, N):
    final_list = []
    op = list1
    for i in range(0, N): 
        max1 = 0
          
        for j in range(len(op)):     
            if op[j] > max1:
                max1 = op[j]
                  
        
        final_list.append(max1) 
        op.pop(j)
          
    return final_list
  
 
  
# Calling the function


from collections import deque
def csAverageOfTopFive(scores):
    fs = deque()
    # fs.append((0, [0]))
    # fs.push(scores)
    # nn = Node()
    tv = []
    ones = []
    twos = []
    for i in scores:
        # print(i)
        # if type(item) in [list, tuple, set]:
        for ii in i:
            # get only 1 or 2s into seprate lists
            if ii == 1:
                ones.append(i[1])
            elif ii == 2:
                
                twos.append(i[1])
            print(ii)
    # top5ones = []
    # top52s = []
    
    
    top51s  = sorted(ones)[:5]
    top52s  = sorted(twos)[:6]
    ta1 = 0
    ta2 = 0
    d1h = 0
    h2h = 0
    for z in top51s:
        d1h = d1h + z
    de = d1h/5
    e1  = takeClosest(de,top51s)
    # twos
    for z in top52s:
        h2h = h2h + z
    d0 = h2h/5
    e2  = takeClosest(d0,top52s)
    dr = [1,e1]
    er = [2,e2]
    su = []
    su.append(dr)
    su.append(er)
    return su
    
def takeClosest(num,collection):
   return min(collection,key=lambda x:abs(x-num))
