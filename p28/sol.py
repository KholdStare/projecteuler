#!/usr/bin/python
import os
import sys
thisDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(thisDir + "/../utils")

from seriesutils import partial_sum, partial_sum_squares
from math import ceil

def partial_sum_odd_squares(terms):
    return sum( ( (2*i + 1) ** 2 for i in xrange(0, terms+1) ) )

def main (dim):
    """ For dim by dim spiral. """
    levels = int(ceil(dim/2.0))
    oddSquareSum = partial_sum_odd_squares(levels-1)

    return 4*oddSquareSum - 12*partial_sum(levels-1) - 3

if __name__ == "__main__":
    print main(1001)
