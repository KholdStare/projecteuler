#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import gen_fibonacci

def main(limit):
    result = 0
    for f in gen_fibonacci():
        if f > limit:
            break

        if f % 2 == 0:
            result += f

    return result

if __name__ == "__main__":
    print main(4e6)
