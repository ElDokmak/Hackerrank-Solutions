#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Frequencies
    count = Counter(s)
    
    # All letters have the same frequency 
    if len(set(count.values())) == 1 :
        return 'YES'
    
    # Two or more have different frequencies
    elif len(set(count.values())) > 2 :
        return 'NO'
    
    # 2 uniqe frequencies
    else :
        for key in count : 
            count[key] -= 1
            temp = list(count.values())
            # Removing zeros from the list if it exist
            try :
                temp.remove(0)
            # else pass
            except :
                pass 
            if len(set(temp)) == 1 :
                return 'YES'
            else :
                count[key] += 1
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
