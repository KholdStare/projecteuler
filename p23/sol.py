#!/usr/bin/python
import os
import sys
thisDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(thisDir + "/../utils")

from numutils import is_abundant, is_abundant_splittable
from seriesutils import sum_consecutive_nums, partial_sum

def main ():
    abundantLimit = 28123
    primes = []
    abundants = [12]

    splittableSum = 0
    for n in xrange(13, abundantLimit+1):
        if is_abundant(n, primes):
            abundants.append(n)

        if is_abundant_splittable(n, primes, abundants):
            splittableSum += n

    totalSum = partial_sum(abundantLimit)
    print "splittableSum: %d, total sum: %d" % (splittableSum, totalSum)

    return totalSum - splittableSum


if __name__ == "__main__":
    print main()
