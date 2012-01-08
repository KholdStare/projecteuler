#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import is_amicable

def main (end):
    primes = []
    sumAmicable = 0

    for n in xrange(2, end):
        if is_amicable(n, primes):
            sumAmicable += n

    return sumAmicable


if __name__ == "__main__":
    print main(10000)
