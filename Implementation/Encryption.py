#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def encryption(s):
    lens = len(s)
    mini = math.floor(math.sqrt(lens))
    maxi = math.ceil(math.sqrt(lens))
    sen = []

    for i in range(maxi):
        j = 0
        temp = []
        while i+j < lens:
            temp.append(s[i+j])
            j += maxi
        sen.append("".join(temp))

    return " ".join(sen)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
