#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
   positive_count = 0
   negative_count = 0
   zero_count = 0
   for i in range(len(arr)):
       if arr[i] > 0:
           positive_count += 1
       elif arr[i] < 0:
            negative_count += 1
       else:
            zero_count += 1
   length = len(arr)
   p_ratio = positive_count / length
   n_ratio = negative_count / length
   z_ratio = zero_count / length
   print("{0:.6f}".format(p_ratio))
   print("{0:.6f}".format(n_ratio))
   print("{0:.6f}".format(z_ratio))
   return 0
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
