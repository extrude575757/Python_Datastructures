from collections import deque
class MyHashSet:
    def __init__(self):
        self.arr = [False] * 10000
        
    def hashIndex(self,key):
        return hash(key) % len(self.arr)
        
    def add(self, key:int) -> None:
        hashIndex = self.hashIndex(key)
        if self.arr[hashIndex] == False:
            newList = deque()
            newList.append(key)
            self.arr[hashIndex] = newList
        elif key not in self.arr[hashIndex]:
            self.arr[hashIndex].append(key)
            
    def remove(self,key:int) -> None:
        hashIndex = self.hashIndex(key)
        if self.arr[hashIndex] is not None:
            try:
                self.arr[hashIndex].remove(key)
            except:
                pass
                
                
                
                
    def contains(self,key:int) -> bool:
        hashIndex = self.hashIndex(key)
        if self.arr[hashIndex] is not None:
            return key in self.arr[hashIndex]
        return False
                



# Count how many times the word lambda is in a string
  
import sys
  
# Function to find the count
def findCount(str1, str2):
  
    len1 = len(str1)
    len2 = len(str2)
    ans = sys.maxsize
  
    # Initialize hash for both strings
    hash1 = [0] * 26
    hash2 = [0] * 26
  
    # hash the frequency of letters of str1
    for i in range(0, len1):
        hash1[ord(str1[i]) - 97] = hash1[ord(str1[i]) - 97] + 1
  
    # hash the frequency of letters of str2
    for i in range(0, len2):
        hash2[ord(str2[i]) - 97] = hash2[ord(str2[i]) - 97] + 1
          
    # Find the count of str2 constructed from str1
    for i in range (0, 26):
        if (hash2[i] != 0):
            ans = min(ans, hash1[i] // hash2[i])
  
    # Return answer
    return ans
  




def count_word(text,word):
    """
    iterate threw scrambled word if one letter is in it remove it and place in array
    
    """
    answer = text
    count = 0
    cc = 0
    ini = []
    ae = ''
    while cc < len(text) -1 :
        if text[:1] == 'a':
            ae = 'a'
        cc = cc + 1
    return ae


def csMaxNumberOfLambdas(text):

    l = 'lambda'
      
    return findCount(text, l)
                
                
                
                

