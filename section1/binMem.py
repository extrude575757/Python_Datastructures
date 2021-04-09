

def toLowerCase(self, str: str) -> str:
    encodedChars = [ord(x) for x in str]
    for i in range(len(encodedChars)):
        if 64 < encodedChars[i] < 91:
            encodedChars[i] += 32
        decodedChars = [chr(x) for x in encodedChars]
        return ''.join(decodedChars)



   #Reverse the binary output of n and convert it to decimal int

def csReverseIntegerBits(n):

    if n == 0:
        
        return n
    print("{0:b}".format(10))   
    binaryNum = "{0:b}".format(n)
    rvBin = binaryNum[::-1] # Reversed it
    #convert from reversedBinary to decimal
    decimal = 0
    # for digit in rvBin:
    #     decimal = decimal*2 + int(digit)
    decimal = int(rvBin,2)
    return decimal

# Convert 8bit binary translation to individual chars
def csBinaryToASCII(binary):

    if binary == 0: 
        return ''
        
    

    split_strings = []
    n  = 8
    for index in range(0, len(binary), n):
        split_strings.append(binary[index : index + n])

    print(split_strings)
    nd = []
    for z in split_strings:
        ss = str(z)
        nd.append('0b'+ss)
    fas = []
    for zz in nd:
        ss = int(zz,2)
        fas.append(ss)
    inf = ''
    for zt in fas:
        
        # n = int(nd, 8)
        inf = inf + zt.to_bytes((zt.bit_length() + 7) // 8, 'big').decode()

    return inf


    """
    Given a number, write a function that converts that number into a string that contains "raindrop sounds" corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operator.

    Here are the rules for csRaindrop. If the input number:

    has 3 as a factor, add "Pling" to the result.
    has 5 as a factor, add "Plang" to the result.
    has 7 as a factor, add "Plong" to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.
    Examples:

    csRaindrops(28) -> "Plong"
    28 has 7 as a factor, but not 3 or 5.
    csRaindrops(30) -> "PlingPlang"
    30 has both 3 and 5 as factors, but not 7.
    csRaindrops(34) -> "34"
    34 is not factored by 3, 5, or 7.
    [execution time limit] 4 seconds (py3)

    [input] integer number

    [output] string

    """ 

def csRaindrops(number):
    
   lsl = []
   print("The factors of",number,"are:")
   for i in range(1, number + 1):
       if number % i == 0:
           lsl.append(i)
   ll = []
   for ii in lsl:
       if ii == 3:
           ll.append('Pling')
       elif ii == 5:
           ll .append('Plang')
       elif ii == 7: 
           ll.append('Plong')
   stree = ''
   for i in ll:
       if i == 'Pling' or i == 'Plang' or i == 'Plong':
           stree = stree + i
   if len(stree) < 1:
       stree = str(number)
   return stree
 


def hammingWeight(self, n: int) -> int:
    return bin(n).count('1')
