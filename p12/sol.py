#!/usr/bin/python
# allow importing from utils
import sys
import os
import operator
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import gen_triangle, gen_factorization, count_occurances

def count_divisors(n, primeList):
    """Get prime factorization, and count all possible combination of those
    prime factors"""
    countDict = count_occurances(gen_factorization(n, primeList))

    # just the counts of the prie factors, not the facors themselves
    # we dont care about them anymore
    countList = countDict.values()

    return reduce(operator.mul, (d+1 for d in countList) , 1)

def main (maxDivisors):
    primeList = []
    for t in gen_triangle():
        if count_divisors(t, primeList) > maxDivisors:
            return t

if __name__ == "__main__":
    print main(500)
