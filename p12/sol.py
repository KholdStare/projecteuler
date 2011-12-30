#!/usr/bin/python
# allow importing from utils
import sys
import os
import operator
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import gen_triangle, gen_factorization, gen_sequence_to_n, gen_subset, count_occurances

def count_divisors(n, primeList):
    """Get prime factorization, and count all possible combination of those
    prime factors"""
    countDict = count_occurances(gen_factorization(n, primeList))

    # just the counts of the prie factors, not the facors themselves
    # we dont care about them anymore
    countList = countDict.values()
    
    count = 1
    # need to generate every possible combination of these counts and find their products
    for combination in gen_subset(countList):
        count += reduce(operator.mul, combination, 1)

    return count

def main (maxDivisors):
    primeList = []
    for t in gen_triangle():
        if count_divisors(t, primeList) > maxDivisors:
            return t

if __name__ == "__main__":
    print main(500)
