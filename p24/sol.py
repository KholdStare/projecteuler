#!/usr/bin/python
import os
import sys
thisDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(thisDir + "/../utils")

from combinatorics import factorial
from math import floor

def find_nth_lexicographic_ordering(symbolList, n, outputSoFar):
    """Given a list of symbols in lexicographic order, find the nth lexicographic
    ordering of the symbols, where n starts from 0."""
    l = len(symbolList)
    if l == 1:
        return outputSoFar + symbolList[0]

    i = int(floor(n / factorial(l-1)))

    # make sure we are within bounds- ie, if the nth ordering is possible
    if i > l:
        return outputSoFar
    
    outputSoFar += symbolList.pop(i)

    return find_nth_lexicographic_ordering(symbolList, n % factorial(l-1), outputSoFar)

def main (maxDigit, n):
    symbolList = [ str(d) for d in xrange(0, maxDigit+1) ]

    return find_nth_lexicographic_ordering(symbolList, n-1, "")

if __name__ == "__main__":
    print main(9, 1e6)
