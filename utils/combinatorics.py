import math
import operator
from math import factorial

def sterling_second(n, k):
    """For a collection of n distinct elements, find the number of k-partitions."""
    if n == 0 or n == k:
        return 1
    return sum(( (1 if (j%2 == 0) else -1) * choose(k, j) * ((k-j) ** n) for j in xrange(0, k) )) / factorial(k)

def bell_number(n):
    """For a collection of n distinct elements, find the number of partitions."""
    if n < 2:
        return 1

    return sum( ( sterling_second(n, k) for k in xrange(0, n+1) ) )

def multinomial_coefficient(multisetSizes):
    """For a multiset, find the number of unique permutations."""
    if len(multisetSizes) <= 1:
        return 1

    return factorial(sum(multisetSizes)) / \
           reduce(operator.mul, (factorial(m) for m in multisetSizes), 1)

def choose(n, k):
    """For a collection of n distinct elements, find the number of unique
    unordered sets of size k."""
    return factorial(n) / (factorial(n-k) * factorial(k))

def falling_factorial(x, n):
    return reduce(operator.mul, ( x - j for j in xrange(0, n) ), 1)

def rising_factorial(x, n):
    return reduce(operator.mul, ( x + j for j in xrange(0, n) ), 1)

def gen_sequence_to_n(n):
    """Given n, generate a list of numbers from 0 to n non-inclusive,
    in ascending order, of all sizes."""
    if n < 1:
        return
    elif n == 1:
        yield [0]
    else:
        yield [n-1]
        for seq in gen_sequence_to_n(n-1):
            newSeq = seq[:]
            yield seq
            newSeq.append(n-1)
            yield newSeq


def gen_subset(bigList):
    """Given some list of elements, generate all subsets of the list."""
    for indexSet in gen_sequence_to_n(len(bigList)):
        yield [ bigList[i] for i in indexSet ]
