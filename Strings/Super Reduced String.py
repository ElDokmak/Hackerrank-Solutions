#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def superReducedString(s):
    res = []

    for i in range(len(s)):
        if len(res) == 0 or res[-1] != s[i]:
            res.append(s[i])
        else:
            res.pop()

    if len(res) == 0:
        return "Empty String"
    else:
        return "".join(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
