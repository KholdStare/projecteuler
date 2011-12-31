#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

#from decoratorutils import memoized

def problem_rule(n):
    if n <= 1:
        return None
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

memoization = {}
def count_sequence_steps(n, rule):
    origN = n
    count = 0

    while n is not None:
        if memoization.has_key(n):
            count += memoization[n]
            n = None
        else:
            n = rule(n)
            count += 1

    memoization[origN] = count
    return count

def main (limit):
    maxCount = 1
    maxN = 1
    
    for n in xrange(1, int(limit)):
        print n
        count = count_sequence_steps(n, problem_rule) 
        if count > maxCount:
            maxCount = count
            maxN = n

    return maxN


if __name__ == "__main__":
    print main(1e6)
