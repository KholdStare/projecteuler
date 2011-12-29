#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import gen_factorization

def count_occurances(numList):
    countDict = {}
    for n in numList:
        if n in countDict:
            countDict[n] += 1
        else:
            countDict[n] = 1

    return countDict

def main(number):
    nums_to_consider = range(2, number+1)
    # How many times a prime is used to compose a given number in the list
    primeUsage = {}

    for num in nums_to_consider:
        primeUsage[num] = 0
        countDict = count_occurances(gen_factorization(num))
        for dPrime in countDict.iterkeys():
            primeUsage[dPrime] = max(countDict[dPrime], primeUsage[dPrime])

    result = 1
    for key in primeUsage:
        if primeUsage[key]:
            result *= (key ** primeUsage[key])

    return result

if __name__ == "__main__":
    print main(20)
