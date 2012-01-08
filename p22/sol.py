#!/usr/bin/python
import os
import sys
thisDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(thisDir + "/../utils")

aVal = ord('A') -1

def alphabetical_value(text):
    return sum(( ord(char) - aVal for char in list(text) ))

def main (filename):
    inputFile = open(filename, 'r')
    # list of lists, indexed like matrix. rows then cols
    names = sorted([ name[1:-1] for name in inputFile.read().split(",") ])
    inputFile.close()
    pos = 0
    totalScore = 0
    for name in names:
        pos += 1 # only increase alpha position if name changed
        totalScore += (pos * alphabetical_value(name))

    return totalScore 

if __name__ == "__main__":
    print main(thisDir + "/names.txt")
