# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    res_arr = []
    for query in queries:
        res_arr.append(strings.count(query))

    return res_arr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = sys.stdout  # stdout is already an open stream

    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]

    res = matchingStrings(strings, queries)
    print(str(res) + '\n')

    # fptr.write(result + '\n')

    # fptr.close()
