#!/usr/bin/python
import os
import operator
thisDir = os.path.dirname(os.path.realpath(__file__))

def get_values(grid, sub):
    """Given a grid and subscript indeces get values for those indeces."""
    return [ grid[sub[i][0]][sub[i][1]] for i in xrange(0,len(sub)) ]

def extend_indeces(start, n, iInc, jInc):
    """Given starting index, using specified increments, construct a set of n indeces."""
    return [ (start[0]+k*iInc, start[1]+k*jInc) for k in xrange(0, n) ]

def gen_dir_indeces(n, m, num, iInc, jInc):
    """Given size of grid and i/j increments, generate sets of indeces for accessing num values
    in the given direction."""

    # define start and end limits given increments

    # if increments go backwards, shift indeces appropriately
    if iInc < 0:
        rowStart = 0+(num-1)*abs(iInc)
        colStart = 0+(num-1)*abs(jInc)
        rowLimit = n
        colLimit = m
    else:
        rowStart = 0
        colStart = 0
        rowLimit = n-(num-1)*abs(iInc)
        colLimit = m-(num-1)*abs(jInc)

    for i in xrange(rowStart, rowLimit):
        for j in xrange(colStart, colLimit):
            yield extend_indeces((i, j), num, iInc, jInc)

def get_prod(numList):
    return reduce(operator.mul, numList, 1)

def get_largest_prod(grid, num, iInc, jInc):
    n = len(grid)
    m = len(grid[0])

    maxProduct = 0
    for i in gen_dir_indeces(n, m, num, iInc, jInc):
        product = get_prod(get_values(grid, i))
        if product > maxProduct:
            maxProduct = product

    return maxProduct


def main (filename):
    inputFile = open(filename, 'r')
    # list of lists, indexed like matrix. rows then cols
    grid  = [ [ int(d) for d in s.strip().split() ] for s in inputFile.readlines() ]

    # all directions
    iIncs = [1, 1, 0, 1]
    jIncs = [0, 1, 1, -1]
    return max([ get_largest_prod(grid, 4, iIncs[k], jIncs[k]) for k in xrange(0, len(iIncs)) ])

if __name__ == "__main__":
    print main(thisDir + "/input")
