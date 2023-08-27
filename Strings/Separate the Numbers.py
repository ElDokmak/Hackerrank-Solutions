#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):
    if len(s) == 1:
        print('NO')
        return

    else:
        for i in range(1, len(s)//2 + 1):  # loop only to the half
            generated_str = s[:i]
            generated_int = int(generated_str)

            # we create our own string and compares it to the original one
            while len(generated_str) < len(s):
                next = generated_int + 1
                generated_str += str(next)
                generated_int = next

            if generated_str == s:
                print('YES', s[:i])
                return

    print('NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
