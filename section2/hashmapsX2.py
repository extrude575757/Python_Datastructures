"""
Find all isomorphic matches.
"""
# Python program to check if two strings are isomorphic
MAX_CHARS = 256
 
# This function returns true if str1 and str2 are isomorphic
def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)
 
    # Length of both strings must be same for one to one
    # corresponance
    if m != n:
        return False
 
    # To mark visited characters in str2
    marked = [False] * MAX_CHARS
 
    # To store mapping of every character from str1 to
    # that of str2. Initialize all entries of map as -1
    map = [-1] * MAX_CHARS
 
    # Process all characters one by one
    for i in range(n):
 
        # if current character of str1 is seen first
        # time in it.
        if map[ord(string1[i])] == -1:
 
            # if current character of st2 is already
            # seen, one to one mapping not possible
            if marked[ord(string2[i])] == True:
                return False
 
            # Mark current character of str2 as visited
            marked[ord(string2[i])] = True
 
            # Store mapping of current characters
            map[ord(string1[i])] = string2[i]
 
        # If this is not first appearance of current
        # character in str1, then check if previous
        # appearance mapped to same character of str2
        elif map[ord(string1[i])] != string2[i]:
            return False
 
    return True
 




def csIsomorphicStrings(a, b):

    return areIsomorphic(a,b)
    
    
    
    
    
    
    
    
    
    
    
    
    
"""
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in a.

Example 1:

Input:
pattern = "abba"
a = "lambda school school lambda"

Output: true
Example 2:

Input:
pattern = "abba"
a = "lambda school school coding"

Output:
false
Example 3:

Input:
pattern = "aaaa"
a = "lambda school school lambda"

Output: false
Example 4:

Input:
pattern = "abba"
a = "lambda lambda lambda lambda"

Output: false
Notes:

pattern contains only lower-case English letters.
a contains only lower-case English letters and spaces ' '.
a does not contain any leading or trailing spaces.
All the words in a are separated by a single space.
[execution time limit] 4 seconds (py3)

[input] string pattern

[input] string a

[output] boolean    
"""    

MAX_CHARS = 256
 
# This function returns true if str1 and str2 are isomorphic
def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)
    
    
        
    # Length of both strings must be same for one to one
    # corresponance
    if m != n:
        return False
 
    # To mark visited characters in str2
    marked = [False] * MAX_CHARS
 
    # To store mapping of every character from str1 to
    # that of str2. Initialize all entries of map as -1
    map = [-1] * MAX_CHARS
    
    
 
    # Process all characters one by one
    for i in range(n):
        if string1[i] == string2[i] and m == n:
            return True
 
        # if current character of str1 is seen first
        # time in it.
        elif map[ord(string1[i])] == -1:
 
            # if current character of st2 is already
            # seen, one to one mapping not possible
            if marked[ord(string2[i])] == True:
                return False
 
            # Mark current character of str2 as visited
            marked[ord(string2[i])] = True
 
            # Store mapping of current characters
            map[ord(string1[i])] = string2[i]
 
        # If this is not first appearance of current
        # character in str1, then check if previous
        # appearance mapped to same character of str2
        
        elif map[ord(string1[i])] != string2[i]:
            return False
            
        
 
    return True
 





def csWordPattern(pattern, a):
 
    return areIsomorphic(pattern,a)
    
    
    
    
    
"""
Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input:
strs = ["apt","pat","ear","tap","are","arm"]

Output:
[["apt","pat","tap"],["ear","are"],["arm"]]
Example 2:

Input:
strs = [""]

Output:
[[""]]
Example 3:

Input:
strs = ["a"]

Output:
[["a"]]
Notes:

strs[i] consists of lower-case English letters.
[execution time limit] 4 seconds (py3)

[input] array.string strs

[output] array.array.string
"""

def csGroupAnagrams(input):


      
    # empty dictionary which holds subsets 
    # of all anagrams together 
    dict = {} 
  
    # traverse list of strings 
    for strVal in input: 
          
        # sorted(iterable) method accepts any 
        # iterable and rerturns list of items 
        # in ascending order 
        key = ''.join(sorted(strVal)) 
          
        # now check if key exist in dictionary 
        # or not. If yes then simply append the 
        # strVal into the list of it's corresponding 
        # key. If not then map empty list onto 
        # key and then start appending values 
        if key in dict.keys(): 
            dict[key].append(strVal) 
        else: 
            dict[key] = [] 
            dict[key].append(strVal) 
  
    # traverse dictionary and concatenate values 
    # of keys together 
    output = list()
    for key,value in dict.items(): 
        output.append(value)
  
    return output 