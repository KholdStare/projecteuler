#!/usr/bin/python
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

import bigops

def main (n):
    # calculate factorial
    digits = bigops.mul_sequence(( bigops.int_to_list(d) for d in xrange(1, n+1) ))
    return sum(digits)

if __name__ == "__main__":
    print main(100)
