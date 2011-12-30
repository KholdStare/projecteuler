#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import gen_triangle, gen_divisors

def count_divisors(n):
    count = 0
    for d in gen_divisors(n):
        count+=1

    return count

def main (maxDivisors):
    maxCount = 0
    for t in gen_triangle():
        print
        print "Triangle Num:"
        print t
        divCount = count_divisors(t)
        print "Count: "
        print divCount
        if divCount > maxCount:
            maxCount = divCount
        print "MaxCount: "
        print maxCount
        if divCount > maxDivisors:
            return t

if __name__ == "__main__":
    print main(500)
