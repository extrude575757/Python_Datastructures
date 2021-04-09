def csAlphanumericRestriction(input_str):
    if(input_str.isalpha()):
        return True
    elif(input_str.isnumeric()):
        return True
    else:
        return False

print(csAlphanumericRestriction('hi'))


def longest(str1, str2):

    # make sure theres no repeats in each string
    plan = ''
    c = 0
        # if len(str1) > len(str2):
        #     for a in str2:
        #         c = c + 1
        #         if a != str1[:c]
        #             plan = plan + a


        # return plan
    
    go = True
    
    while c < len(str2): 
        
        for d in str1:
            if str2[c] != d:
                plan = plan + d
               
            else: 
                 c = c+ 1
                
                
    # combine all letters once

print(longest('asf', 'b'))