
# Square all digits 

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
        

