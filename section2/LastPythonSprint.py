"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

[output] char

The first non-repeating character in s of '_' if there are no characters that do not repeat.
"""

NO_OF_CHARS = 256
 
# Returns an array of size 256 containg count
# of characters in the passed char array
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
 
# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 


def first_not_repeating_character(s):
    
    
    # Driver program to test above function
    
    index = firstNonRepeating(s)
    if index == -1:
        return '_'
    else:
        return s[index]
    
    # notin = '_'
    # if firstNonRepeating(s) == 0:
    #     return notin
    # else:
    #     return firstNonRepeating(s)


"""
Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer node

The head node of the linked list.

[output] linkedlist.integer

The head node of the updated linked list.

[Python 3] Syntax Tips
"""
#########33 the one that worked with all 100%

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.head = None
    self.next = None
    
  def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next

class LinkedList(object):
    def __init__(self):
        self.head = None


def removeDup(input_str):
    

    a=' '.join(unique_list(input_str.split()))
    return
    
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
    
    
def condense_linked_list(node):
    nn = []
    ll  = LinkedList()
    count = 0
    while node:
        if count == 0:
            
            ll.head = node.value
            nn.append(node.value)
            # node = node.value
        else:
            nn.append(node.value)
        count +=1
         
        node=node.next
        # node = node.head    
    
    
    return unique_list(nn)
    





"""
In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
Example 2:

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3
Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
Example 3:

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.
Example 4:

Input: n = 3, trust = [[1, 2], [2, 3]]
Output: -1
Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.
Example 5:

Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
Output: 3
Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts Person 3 but Person 3 does not trust anyone, so they are the spy.
[execution time limit] 4 seconds (py3)

[input] integer n

The number of people in the city-state

[input] array.array.integer trust

Array of pairs indicating who each person in trusts.

[output] integer

The identifier of the spy.


"""







def uncover_spy(n, trust):
    wa = []
    if len(trust) <= 10:
        for i, ff in enumerate(trust):
            if len(trust) == 1:
                for fz in ff:
                    if ff[i+1] != n and ff[i] == n:
                        return -1
                    elif ff[i+1] == n:
                        return n
                     
            else:
                for fz in ff:
                    if fz == n:
                        return i
                    elif fz != n and i < len(trust) -1 :
                        return -1
            if i == len(trust):
            
                        return n
    # return trust
    




