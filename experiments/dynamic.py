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

def optimum(intervalList, i, compatibleIndeces, optArray):

    if i == -1:
        return 0

    # calculate result if not yet calculated
    if optArray[i] == 0:
        p_i = compatibleIndeces[i]

        optArray[i] = max(optimum(intervalList, p_i, compatibleIndeces, optArray) + intervalList[i].value,
                          optimum(intervalList, i-1, compatibleIndeces, optArray))

    return optArray[i]

def main (intervalList):
    # sort list with ascending end times
    sortedList = sorted(intervalList, key=lambda x: x.end)
    n = len(sortedList)

    # for each interval store index of first compatible interval
    compatibleIndeces = [ firstCompatibleIndex(sortedList, i) for i in xrange(0, n) ]

    return optimum(intervalList, n-1, compatibleIndeces, [ 0 for x in xrange(0, n) ])


if __name__ == "__main__":
    # from Kleinberg and Tardos p253
    intervalList = [ Interval(0, 3, 2),
                     Interval(1, 5, 4),
                     Interval(4, 6, 4),
                     Interval(2, 9, 7),
                     Interval(7, 10, 2),
                     Interval(8, 11, 1) ]

    print main(intervalList)
