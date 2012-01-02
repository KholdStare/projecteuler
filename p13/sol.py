#!/usr/bin/python
import os
import sys
thisDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(thisDir + "/../utils")
import bigops

def main (filename):
    inputFile = open(filename, 'r')
    # list of lists, indexed like matrix. rows then cols
    grid  = [ [ int(d) for d in list(s.strip()) ] for s in inputFile.readlines() ]
    inputFile.close()

    return "".join([str(d) for d in bigops.sum_sequence(grid)])

if __name__ == "__main__":
    print main(thisDir + "/input")
