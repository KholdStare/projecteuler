#!/usr/bin/python
import os
thisDir = os.path.dirname(os.path.realpath(__file__))

def main (filename):
    inputFile = open(filename, 'r')
    # list of lists, indexed like matrix. rows then cols
    matrix  = [ [ int(d) for d in s.strip().split(",") ] for s in inputFile.readlines() ]
    inputFile.close()
    
    # modify matrix for easier computation below, so no bounds checking
    largeNum = 9e9 # some number larger than the rest
    for i in xrange(0, len(matrix)-1):
        matrix[i].append(largeNum)
    matrix[-1].append(0)

    lastRow = [ largeNum for i in xrange(0, len(matrix[-1])-1) ] # make the last row large numbers
    lastRow.append(0) # except for the bottom right number
    matrix.append(lastRow)

    for row in xrange(len(matrix)-2, -1, -1):
        for col in xrange(len(matrix[row])-2, -1, -1):
            matrix[row][col] += min(matrix[row+1][col], matrix[row][col+1])

    return matrix[0][0]


if __name__ == "__main__":
    print main(thisDir + "/matrix.txt")
