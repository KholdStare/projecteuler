#!/usr/bin/python

number = 20
nums_to_consider = range(2, number+1)

primes = set()
def is_prime(a):
    """ Returns true if number is a prime. relies on a set of primes,
    and thus needs to be called on numbers in order."""
    if len(primes) == 0:
        return True
    elif all ([ (a % p != 0 and p < a) for p in primes ]):
        return True
    else:
        return False

def prime_decomposition(num, primes):
    """Given a number, and a set of all primes up to that number,
    return a list of the numbers that make up the prime decomposition
    of num """
    ascendingPrimes = sorted(list(primes))
    smallestP = ascendingPrimes.pop(0)
    decomposition = []
    while num != 1:
        if num % smallestP == 0:
            decomposition.append(smallestP)
            num = num / smallestP
        else:
            if len(ascendingPrimes) == 0:
                break

            smallestP = ascendingPrimes.pop(0)

    return decomposition

def count_occurances(numList):
    countDict = {}
    for n in numList:
        if n in countDict:
            countDict[n] += 1
        else:
            countDict[n] = 1

    return countDict

# How many times a prime is used to compose a given number in the list
primeUsage = {}
primeUsage[1] = 1

for num in nums_to_consider:
    if is_prime(num):
        primes.add(num)
        primeUsage[num] = 1
    else:
        decomp = prime_decomposition(num, primes)
        countDict = count_occurances(decomp)
        for dPrime in countDict.iterkeys():
            primeUsage[dPrime] = max(countDict[dPrime], primeUsage[dPrime])

print primeUsage

result = 1
for key in primeUsage:
    result *= (key ** primeUsage[key])

print result
