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

def main (intervalList):
    # sort list with ascending end times
    sortedList = sorted(intervalList, key=lambda x: x.end)


if __name__ == "__main__":
    # from Kleinberg and Tardos p253
    intervalList = [ Interval(0, 3, 2),
                     Interval(1, 5, 4),
                     Interval(4, 6, 4),
                     Interval(2, 9, 7),
                     Interval(7, 10, 2),
                     Interval(8, 11, 1) ]
    print [ x.__str__() for x in intervalList ]

    print '\n'
    random.shuffle(intervalList)
    print [ x.__str__() for x in intervalList ]

    print '\n'
    sortedList = sorted(intervalList, key=lambda x: x.end)
    print [ x.__str__() for x in sortedList ]
    print listValue(intervalList)

