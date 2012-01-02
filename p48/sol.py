#!/usr/bin/python
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

import bigops

def gen_sequence(lastNum):
    for i in xrange(1, lastNum+1):
        print i
        yield bigops.mul_sequence(( bigops.int_to_list(i)[-10:] for d in xrange(1, i+1) ))

def main (lastNum):
    # calculate factorial
    digits = bigops.sum_sequence( gen_sequence(lastNum) )
    return bigops.list_to_str(digits[-10:])

if __name__ == "__main__":
    print main(1000)
