"""
I made sure the list was converted into a string, that way I could use str.[::-1] to reverse the lettering and place it into a list where it will be returned within the function 
I would look into using quadratic formulas so every element iterates through. Depending on the length of each list and how much processing power it takes up in memory binary conversion will enhance the performance within ram. 
"""



def csReverseString(chars):

    ss = ''
    for z in chars:
        ss = ss + z
    st = ss[::-1]
    street = []
    for i in st:
        street.append(i)
    return street

"""
I only compared the input of the string to a reversed version made with [::-1] This used with a conditional statement checking if both strings equal the same characters will return True. Otherwise it returns False. I Figured for this there would be issues with digits but there was no needed conditions as a simple if else block worked for this simple 4 liner. 

Multiple palindromes can be searched for at a time so that only one call is made. If functions need to be called more than once recursive calls can be used to iterate at a max performance rate for the machines ram and CPU. 
"""

def csCheckPalindrome(input_str):
    rv = input_str[::-1]
    if rv == input_str:
        return True
    else:
        return False


"""
I had to make an additional function which got ran with the split method for strings. The additional function called unique_list returns the duplicate strings where each white space joins. With one line within the main function is a string with all duplicate strings . It is very convenient to write and quick to make. 
I would look into using the minimum amount of ram needed for this program to run. It is a one line solution so I if it was tested we would need to know what our performance was for each length of duplicate strings that get tested. If we could assume a comfortable ratio for all devices other program features could be developed to safe guard the application from a crash while gaining optimal performance.  
"""

def csRemoveDuplicateWords(input_str):


    a=' '.join(unique_list(input_str.split()))
    return a
    


def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

