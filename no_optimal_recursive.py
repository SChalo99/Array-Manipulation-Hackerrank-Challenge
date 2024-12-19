#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
#####################################################
# WORKS BUT IT IS NOT AN OPTIMAL SOLUTION
# REVIEW CHALLENGE_DIFFERENCE_ARRAY.PY
#####################################################
def recursive(a,b,k,arr):
    if(a>b):
        return
    arr[a-1] += k
  
    recursive(a+1,b,k,arr)

def arrayManipulation(n, queries):
    arr = [0]*n
    while(len(queries)>0):
        values = queries.pop()
        a = values[0]
        b = values[1]
        k = values[2]
        recursive(a,b,k,arr)
    return max(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
