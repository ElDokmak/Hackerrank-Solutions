#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

# the logic is to find the number of inversion 
# inversion is the numbers on the left that is greater than the one u are on
# for ex 1 3 4 2 for the number 2 there is 2 numbers that are greater (3 and 4)

def larrysArray(A):
    
    count = 0
    
    for i in range(len(A)) :
        for j in range(i+1, len(A)) :
            if A[i] > A[j] :
                count += 1
                
    return 'YES' if count%2 == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
