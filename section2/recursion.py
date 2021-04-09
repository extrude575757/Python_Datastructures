def fibonacciSimpleSum2(n):

    # creating a set containing
    # all fibonacci numbers
    hash1 = set()
    createHash(hash1, n)
 
    if n < 1000:
        # Traversing all numbers
        # to find first pair
        for i in range(n):
 
         # If both i and (N - i) are Fibonacci
         if (i in hash1 and (n - i) in hash1):
 
            # Printing the pair because
            # i + (N - i) = N
            print(i , ", ", (n - i))
            return True
 
    # If no fibonacci pair is found
    # whose sum is equal to n
    return False

    # Python3  program to find two
# Fibonacci numbers whose
# sum can be represented as N
 
# Function to create hash table
# to check Fibonacci numbers
def createHash(hash1,maxElement):
 
    # Storing the first two numbers
    # in the hash
    prev , curr = 0 , 1
    hash1.add(prev)
    hash1.add(curr)
 
    # Finding Fibonacci numbers up to N
    # and storing them in the hash
    while (curr < maxElement):
        temp = curr + prev
        hash1.add(temp)
        prev = curr
        curr = temp
 


 
   
     

