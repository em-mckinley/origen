#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    am_dict = {
        "12" : "00",
        "01": "01",
        "02": "02",
        "03": "03",
        "04": "04",
        "05": "05",
        "06": "06",
        "07": "07",
        "08": "08",
        "09": "09",
        "10": "10",
        "11": "11"
    }
    pm_dict = {
        "12" : "12",
        "01": "13",
        "02": "14",
        "03": "15",
        "04": "16",
        "05": "17",
        "06": "18",
        "07": "19",
        "08": "20",
        "09": "21",
        "10": "22",
        "11": "23"
    }

    time_converted = ""
    #Compare last two char
    if s[8:10] == 'AM':
        #grab the corresonding time
        time_converted = am_dict[s[0:2]] + s[2:8]
    else:
        time_converted = pm_dict[s[0:2]] + s[2:8]
    return time_converted


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #fptr = sys.stdout  # stdout is already an open stream

    #s = input()
    s = '12:01:00PM'
    result = timeConversion(s)
    print(str(result) + '\n')
    s = '03:01:00AM'
    result = timeConversion(s)
    print(str(result) + '\n')

    #fptr.write(result + '\n')

    #fptr.close()