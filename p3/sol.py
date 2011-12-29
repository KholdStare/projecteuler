#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import gen_factorization

def main (limit):
    for n in gen_factorization(limit):
        largestFactor = n

    return largestFactor

if __name__ == "__main__":
    print main(600851475143)
