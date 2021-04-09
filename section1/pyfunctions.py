
   """
        Create a function that returns True if the given string has any of the following:

        Only letters and no numbers.
        Only numbers and no letters.
        If a string has both numbers and letters or contains characters that don't fit into any category, return False.

        Examples:

        csAlphanumericRestriction("Bold") ➞ True
        csAlphanumericRestriction("123454321") ➞ True
        csAlphanumericRestriction("H3LL0") ➞ False
        Notes:

        Any string that contains spaces or is empty should return False.
        [execution time limit] 4 seconds (py3)

        [input] string input_str

        [output] boolean

        [Python 3] Syntax Tips

        # Prints help message to the console
        # Returns a string
        def helloWorld(name):
        print "This prints to the console when you Run Tests"
        return "Hello, " + name
   
        300/300
   """


def csAlphanumericRestriction(input_str):
    if(input_str.isalpha()):
        return True
    elif(input_str.isnumeric()):
        return True
    else:
        return False

print(csAlphanumericRestriction('hi'))




    # Square all digits  300/300

def csSquareAllDigits(n):
    res = [int(x) for x in str(n)] 
    print(res)
    multiplied_list = [element * element for element in res]
    str1 = ''
    print(multiplied_list)
    for e in multiplied_list:  
        str1 +=  str(e)
    print(str1)
    numCon = int(str1)   
    return numCon
        

    """
    Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

        Examples:

        csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
        csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
        csOppositeReverse("Radar") ➞ "RADAr"
        Notes:

        The input string will only contain alpha characters.
        [execution time limit] 4 seconds (py3)

        [input] string txt

        [output] string

        [Python 3] Syntax Tips

        # Prints help message to the console
        # Returns a string
        def helloWorld(name):
        print "This prints to the console when you Run Tests"
        return "Hello, " + name
    
        20/300
    """



def csOppositeReverse(txt):
    
    newStr = ''
    nw = ''
    for ch in txt:
        if(ch.isupper()):
            newStr = ''.join(ch.lower())
        else:
            newStr = ''.join(ch.upper())
    print(sorted(newStr, reverse=True))
    newLen = len(newStr)
    for c in newStr:
        nw = c + nw.join( newStr[newLen : -newLen])
        newLen = newLen -1
     
    return nw
    
 
        
print(csOppositeReverse('Hello World'))


    # Remove the vowels


def csRemoveTheVowels(text): 
        vowles = ("aeiouAEIOU")
        for i in vowles :
            text = text.replace(i,"")
        return text

    # print csRemoveTheVowels("why")







    """
    Given an array of integers, return the sum of all the positive integers in the array.

    Examples:

    csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
    csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
    csSumOfPositive([-3, -2]) -> 0
    Notes:

    If the input_arr does not contain any positive integers, the default sum should be 0.
    [execution time limit] 4 seconds (py3)

    [input] array.integer input_arr

    [output] integer

    """


def csSumOfPositive(input_arr):
    p = 0
    # newlist = [n if n > 0 else None for n in numbers]
    newlist = [n for n in input_arr if n > 0]
    for x in newlist:
        p = p + x
    return p



    """
    Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

    Examples:

    csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
    csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
    csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
    Notes:

    The output can contain the digit 5.
    The start number will always be less than the end number (both numbers can also be negative).
    [execution time limit] 4 seconds (py3)

    [input] integer start

    [input] integer end

    [output] integer

    [Python 3] Syntax Tips
    
    """


def csAnythingButFive(start, end):
    c = 0
    
    while start <= end: 
        
        if '5' in str(start):
            pass
        else: 
            c = c + 1
        start = start + 1
    return c


