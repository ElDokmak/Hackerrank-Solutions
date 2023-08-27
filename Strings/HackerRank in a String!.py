#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def hackerrankInString(s):
    target = 'hackerrank'
    n = len(target)
    i = 0

    for char in s:
        if char == target[i]:
            i += 1
            if i == n:
                return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
