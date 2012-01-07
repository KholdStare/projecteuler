import combinatorics

def is_prime(a, primes):
    """ Returns true if number is a prime. Relies on a set of primes,
    and thus needs to be called on numbers in order."""
    if len(primes) == 0:
        return True

    upperBound = int((a ** 0.5) + 1)
    for p in primes:
        if a % p == 0:
            return False
        if p > upperBound:
            return True

    return True

def gen_fibonacci():
    """Generates fibonacci numbers as 1, 1, 2, 3, 5 ..."""
    a = 0
    b = 1
    yield b
    while 1 == 1:
        c = a + b
        yield c
        a = b
        b = c

def gen_natural_numbers(start = 0, end = -1, incr = 1):
    """Generates natural numbers from start to end, with increments of inc.
    If end is less than 0, generates infinitely."""
    i = start
    sign = incr // abs(incr)
    while end < 0 or i*sign <= end*sign:
        yield i
        i += incr

def gen_prime_numbers(end = -1):
    """Generates prime numbers."""
    yield 2
    yield 3
    primeList = [2, 3]
    for n in gen_natural_numbers(5, end, 6):
        if is_prime(n, primeList):
            primeList.append(n)
            yield n

        n=n+2
        if is_prime(n, primeList) and (end < 0 or n <= end):
            primeList.append(n)
            yield n
                
def gen_triangle(end = -1):
    """Generate triangle numbers: 1 + 2 + 3 + ..."""
    n = 0
    for i in gen_natural_numbers(1, end):
        n += i
        yield n


def extend_primes(primeList, end):
    """Given list of primes, extend to end. Modifies in place"""
    if len(primeList) == 0:
        lastPrime = 1
    else:
        lastPrime = primeList[-1]

    if lastPrime >= end:
        return # dont need to do anything

    if lastPrime < 2:
        primeList.append(2)
    if lastPrime < 3:
        primeList.append(3)

    lastPrime = primeList[-1]

    # find where to resume searchng for primes
    if lastPrime > 3 and lastPrime % 6 == 5:
        n = lastPrime+2
        if is_prime(n, primeList):
            primeList.append(n)
        startPoint = lastPrime+6
    elif lastPrime == 3:
        startPoint = 5
    else:
        startPoint = lastPrime+4
    
    # start finding primes
    for n in xrange(startPoint, end, 6):
        if is_prime(n, primeList):
            primeList.append(n)

        n=n+2
        if is_prime(n, primeList) and n <= end:
            primeList.append(n)



def gen_factorization(n, primes = None):
    """Given a number generate the numbers that make up the prime factorization
    of n """
    bound = int(n ** 0.5)+1
    if primes == None:
        primeIterable = gen_prime_numbers(bound)
    else:
        primeIterable = primes
        extend_primes(primes, bound)

    for p in primeIterable:
        if p*p > n: break
        while n % p == 0:
            yield p
            n //= p
    if n > 1: yield n

def count_occurances(numIter):
    countDict = {}
    for n in numIter:
        if n in countDict:
            countDict[n] += 1
        else:
            countDict[n] = 1

    return countDict

def _gen_divisors(countList, primeFactors):
    if len(countList) == 0:
        yield 1
        return

    count = countList.pop()
    prime = primeFactors.pop()

    for div in _gen_divisors(countList, primeFactors):
        yield div
        for p in xrange(0, count):
            div *= prime
            yield div


def gen_divisors(n, primes = None):
    countDict = count_occurances(gen_factorization(n, primes))

    countList = countDict.values()
    primeFactors = countDict.keys()
    return _gen_divisors(countList, primeFactors)


