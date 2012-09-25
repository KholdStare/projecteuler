#!/usr/bin/env python
import os
import sys
thisDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(thisDir + "/../utils")

from numutils import extend_primes
from listutils import binary_search

def gen_rotations(num):
    """Generates rotations of a number's digits
    (not including the number itself)
    """

    numStr = str(num)

    for i in xrange(1, len(numStr)):
        yield int( numStr[i:] + numStr[0:i] )

def gen_circular_primes(primeList, bound):
    """Generate circular primes until the bound is reached.
    """
    extend_primes(primeList, bound)

    for p in primeList:
        # test if circular

        isCircular = True
        for rot in gen_rotations(p):
            if binary_search(rot, primeList) < 0:
                isCircular = False
                break

        if isCircular:
            yield p


def main(upperBound):
    primeList = [2, 3]
    return len([ n for n in gen_circular_primes(primeList, upperBound) ])


if __name__ == "__main__":
    print main(1000*1000)

