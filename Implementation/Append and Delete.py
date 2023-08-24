#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s, t, k):
    count = 0

    # Calculating the matching characters
    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    total_len = len(s) + len(t)

    if total_len <= 2*count + k and total_len % 2 == k % 2 or total_len < k:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
