#!/usr/bin/python
import os
import operator
thisDir = os.path.dirname(os.path.realpath(__file__))

def main (filename):
    inputFile = open(filename, 'r')
    digits = [ int(d) for s in inputFile.readlines() for d in list(s.strip()) ]
    inputFile.close()
    largestProduct = 0

    for i in xrange(0, len(digits)-5):
        product = reduce(operator.mul, digits[i:i+5], 1)
        if product > largestProduct:
            largestProduct = product

    return largestProduct

if __name__ == "__main__":
    print main(thisDir + "/input")
