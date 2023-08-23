#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    maxnum = 0
    minnum = 9999999999999999
    for i in range(len(arr)):
        sumi = sum(arr)
        minnum = min(minnum, arr[i])
        maxnum = max(maxnum, arr[i])

    print(sumi-maxnum, sumi-minnum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
