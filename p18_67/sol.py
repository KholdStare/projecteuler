#!/usr/bin/python
import os
thisDir = os.path.dirname(os.path.realpath(__file__))

def main (filename):
    inputFile = open(filename, 'r')
    # list of lists, indexed like matrix. rows then cols
    pyramid  = [ [ int(d) for d in s.strip().split() ] for s in inputFile.readlines() ]
    inputFile.close()

    for row in xrange(len(pyramid) - 2, -1, -1):
        for col in xrange(0, len(pyramid[row])):
            pyramid[row][col] += max(pyramid[row+1][col], pyramid[row+1][col+1])

    return pyramid[0][0]


if __name__ == "__main__":
    print main(thisDir + "/input_67")
