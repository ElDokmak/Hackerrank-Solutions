#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # initialize the array but notice that 
    # the index is starting from 0 not 1 
    # so use arr[1:]
    arr = [x for x in range(n+1)]
    
    # test case 2 and 3 above
    if k == 0 :
        return arr[1:]
    if n % 2 == 1 :
        return [-1]
    
    for i in range(1, n+1-k) :
        if arr[i] == arr[i+k] - k :
            arr[i], arr[i+k] = arr[i+k], arr[i]
        elif abs(arr[i] - i) != k :
            return [-1]
    for i in range(n+1-k, n+1) :
        if abs(arr[i] - i) != k :
            return [-1]
        
    return arr[1:]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
