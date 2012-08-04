#!/usr/bin/env python
# allow importing from utils
import sys
import os
import random
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

###########################################################################
#                     dynamic programming experiments                     #
###########################################################################

class Interval(object):
    """Represent an interval with a weight.
    Used for interval scheduling problems"""

    def __init__(self, start, end, value=1):
        self.start = start
        self.end = end
        self.value = value

    def isOverlapping(self, other):
        """Return True if two intervals overlap."""
        return other.start < self.end and self.start < other.end

    def length(self):
        """ :returns: length of interval """
        return self.end - self.start

    def __str__(self):
        return "[ {}, {} ] val:{}".format(self.start, self.end, self.value)

def isValidList(intervalList):
    """ Returns True if the list of intervals is disjoint.
    Assumes sorted by ending time"""

    if len(intervalList) == 0:
        return True

    i = iter(intervalList)
    a = i.next()
    for b in i:
        if a.isOverlapping(b):
            return False

        a = b

    return True
        
def listValue(intervalList):
    """ Returns total value of all intervals. """
    return sum( i.value for i in intervalList )

def firstCompatibleIndex(intervalList, i):
    """ Given a sorted list of intervals, and an index to
    particular interval, return an index j<i such that 
    j.isOverlapping(i) == false.
    If no such interval exists, return -1. """

    if i >= len(intervalList):
        return -1

    interval = intervalList[i]
    j = i-1
    while j >= 0 and intervalList[j].isOverlapping(interval):
        j -= 1

    return j

class WeightedSchedulingProblem(object):
    """Represented a weighted interval schedule problem"""

    def __init__(self, intervalList):
        self.intervalList = sorted(intervalList, key=lambda x: x.end)
        self.n = len(intervalList)
        self.compatibleIndeces = [ firstCompatibleIndex(intervalList, i) for i in xrange(0, self.n) ]

        # careful! off by one indexing so that empty case
        # has a value 
        self.optArray = [ 0 for x in xrange(0, self.n+1) ]

        # construct solution and memoize it
        for i in xrange(0, self.n):
            self.optArray[i+1] = self.calcOptimum(i)

        # reconstruct optimal interval list from optimum value




    def calcOptimum(self, i):
        p_i = self.compatibleIndeces[i]
        return max(self.getOptimum(p_i) + self.intervalList[i].value,
                          self.getOptimum(i-1))

    def getOptimum(self, i):
        return self.optArray[ i+1 ]

    def getOptimumList(self, i=None, acc=[]):

        if i is None:
            return self.getOptimumList(self.n-1)

        if i < 0:
            return acc

        # if the optimum value for this index is the same as
        # for the index below, this interval is not part of the optimal solution
        if self.getOptimum(i) == self.getOptimum(i-1):
            return self.getOptimumList(i-1, acc)

        acc.insert(0, self.intervalList[i])

        p_i = self.compatibleIndeces[i]
        return self.getOptimumList(p_i, acc)


def main (intervalList):
    problem = WeightedSchedulingProblem(intervalList)

    return [ i.__str__() for i in problem.getOptimumList(len(intervalList) - 1) ]


if __name__ == "__main__":
    # from Kleinberg and Tardos p253
    intervalList = [ Interval(0, 3, 2),
                     Interval(1, 5, 4),
                     Interval(4, 6, 4),
                     Interval(2, 9, 7),
                     Interval(7, 10, 2),
                     Interval(8, 11, 1) ]

    print main(intervalList)
