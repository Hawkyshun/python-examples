#!/bin/python

import math
import os
import random
import re
import sys


# write your code here
def avg(*args):
    if not args:
        return 0
    
    if len(args) > 100:
        return 0
    
    if any(not (-100 <= x <= 100) for x in args):
        return 0
    
    result = sum(args) / float(len(args))
    return round(result, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = map(int, raw_input().split())
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
