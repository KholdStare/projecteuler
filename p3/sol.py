#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import is_prime


def gen_natural_numbers(start = 0, end = -1, incr = 1):
    i = start
    while end < 0 or i <= end:
        yield i
        i += incr

    return

def update_primes(start, end, primes):
    """Updates the primes set from last considered number up to the
    given one. Returns True if num is prime as well."""
    for n in gen_natural_numbers(start, end-1, 2):
        if is_prime(n, primes):
            primes.add(n)

    if is_prime(end, primes):
        primes.add(end)
        return True

    return False

def main (limit):
    primes = set([2, 3])
    largestFactor = 3
    prevNum = 3

    for n in gen_natural_numbers(5, limit/2, 2):
        if limit % n == 0:
            print n
            if update_primes(prevNum + 2, n, primes):
                largestFactor = n
            prevNum = n

    return largestFactor

if __name__ == "__main__":
    print main(600851475143)
