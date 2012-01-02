#!/usr/bin/python
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

import bigops

def main (power):
    digits = bigops.mul_sequence( (bigops.int_to_list(2) for d in xrange(1, power+1)) )
    return sum(digits)


if __name__ == "__main__":
    print main(1000)
