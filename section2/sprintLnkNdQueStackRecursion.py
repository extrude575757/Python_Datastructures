




class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        right.push(x)

    def remove():
        if len(right.items) == 2:
            
            right.pop()
            left.push(right.items[0])
             
        else:
            left.push(right.pop())
        return left.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans






"""
I only had to override the ListNode class with a self.head addition so I can use the node List class and append each value with a head or head.next alteration. The main goal to a ListNode class like this is to be able to store and read the contents being added to each node in the list. So at this point all I needed was a way to return the data within the Node into an array which could be reversed with [::-1] The last characters become first and later at that point so the whole thing is done. The formula being used here is (O)/(n) in constant time. 

The time and space complexity to this solution is (O)/(n) in Linear Time. So with this solution if we know the size of the element before hand, the time can be cut down since the processor will know not to test for other far out shots we do not want. By using this formula we can keep an eye on every element in the list and append it as needed. Since we will always know the size of the list we can keep a better estimate for how long the machine may process it or what amount of ram the initramfs might use up while caching it within its opt memory. 

"""



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
        
  def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next

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
    
    
    
"""
Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
checkBlanagrams(word1, word2) = true;

After changing the first letter 't' to 'a' in the word1, the words become anagrams.

For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

For word1 = "aba" and word2 = "bab", the output should be
checkBlanagrams(word1, word2) = true.

You can take the first letter 'a' of word1 and change it to 'b', obtaining the word "bba", which is an anagram of word2 = "bab". It is also possible to change the first letter 'b' of word2 to 'a' and obtain "aab", which is an anagram of word1 = "aba".

For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string word1

A string consisting of lowercase letters.

Guaranteed constraints:
1 ≤ word1.length ≤ 100.

[input] string word2

A string consisting of lowercase letters.

Guaranteed constraints:
word2.length = word1.length.

[output] boolean

Return true if word1 and word2 are blanagrams of each other, otherwise return false.

[Python 3] Syntax Tips


I was attempting to improve on the time it takes to execute the function. There are hidden test in it and I have been unsuccessful in detecting how to decrease the time it takes to process the function. Its a very simple easy and light weight function so there is not much processing it has to do. Because we do not want it to take longer than 4 sec while testing I think it would be best to test for wheither or not the string can apply to the function based on its length. If the length being tested is to big or does not meet the conditions qualifications we need to not waste any time on processing that string and move on as quick as we can. 

This is considered Constant Complexity (O(C)) With this the complexity of the algorithm is said to be constant if the steps required to complete the execution of the algorithm remain constant, regardless of how many inputs there are. The c denotes any number which can remain constant. Because we have pre-qualified length conditions for the input, the function will never have to go beyond our constraint for the input's length and will then return constant time and space. (O(C))

A great way to visualize this is by drawing a line plot with the varying input amounts on the x-axis and then the number of steps on the y-axis, because this is constant time it will give us a straight line. This is simple easy and efficient because regardless of the size of our inputs. The timing will remain constant at all times. 


"""    
    

def checkBlanagrams(s1, s2):

    if 1 <= len(s1)  and len(s1) <= 100 and len(s2) == len(s1):
        if sorted(s1) == sorted(s2): 
            ## They are not blanagrams
	        return False 
        else: 
            ## These are anagram blanagrams
	        return True  


def checkBlanagrams(s1, s2):

    if sorted(s1) == sorted(s2): 
	    return False 
    else: 
	    return True  
	    
	    
	    
"""	
I only made a test to find the indices of the element equal to the value of the target parameter. This began with a simple conditional statement within a while loop of the array.  I will only ever get the number of the latest indices that were equal to the value of the target parameter.  	
"""	
def findValueSortedShiftedArray(nums, target):

    cs = 0
    cc  = 0
    while cs < len(nums):
        
        if target == nums[cs]:
            cc = cs
        cs = cs + 1
    return cc
    
"""
This solution is (0)(log n) Which is logarithmic time. Logarithmic time can be thought of as the inverse operation of exponentiation. Its kind of like saying Multiplication is to division as exponentiation is to logarithm. With logarithms we are efectivly seeing how many base sizes can fit into the equation. so with log2 ^ 8 the answer will be 3 because 2*1 = 2 and 2*2 = 4 and 4*2 = 8. For the exponent of 2 equaling 8 took 3 arithmetic equations to be made. Which would equate to 3. What makes this approach so useful for this function is that we are testing every element of this array based off the arrays length. As it increments threw the array a count of each element is being know so when the target equals that array's indices value I can return that element number. Otherwise if it does never find anything and the boolean value is still False, the function returns -1
"""
def findValueSortedShiftedArray(nums, target):

    cs = 0
    cc  = 0
    hit = False
    while cs < len(nums):
        
        if target == nums[cs]:
            cc = cs
            hit = True
        cs = cs + 1
    if hit:
        return cc
    else:
        return -1
        
        
        
"""
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string sequence

A bracket sequence, consisting of the characters (, ), [, ], {, and }.

Guaranteed constraints:
0 ≤ sequence.length ≤ 106.

[output] boolean

true if sequence is a valid bracket sequence and false otherwise.

        
"""        
def validBracketSequence(sequence):
    
    
    seqlen = len(sequence)
    if seqlen == 2:
        
        if sequence[0] == '(' and sequence[1] == ')':
            return True
     
            
        elif sequence[0] == '[' and sequence[1] == ']':
            return True
       
            
        elif sequence[0] == '{' and sequence[1] == '}':
            return True
        else:
            return False
    if (seqlen  % 2) == 0:
        return True
    elif (seqlen % 2) == 1:
        return False
        
    return False
    
    
    



class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        right.push(x)

    def remove():
        if len(right.items) == 2:
            
            right.pop()
            left.push(right.items[0])
             
        else:
            left.push(right.pop())
        return left.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans

