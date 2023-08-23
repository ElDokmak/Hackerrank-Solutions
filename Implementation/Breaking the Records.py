#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    mini = maxi = 0
    res = [scores[0], scores[0]]
    for i in range(1, len(scores)):
        if scores[i] > res[0]:
            res[0] = scores[i]
            maxi += 1
        elif scores[i] < res[1]:
            res[1] = scores[i]
            mini += 1
    return maxi, mini


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
