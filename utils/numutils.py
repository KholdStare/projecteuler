
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
    prime_list = [2, 3]
    for n in gen_natural_numbers(5, end, 6):
        if is_prime(n, prime_list):
            prime_list.append(n)
            yield n

        n=n+2
        if is_prime(n, prime_list) and (end < 0 or n <= end):
            prime_list.append(n)
            yield n
                
def gen_divisors(n):
    """Given a number generate all divisors of that number"""

    yield 1
    if n == 1:
        return

    for i in xrange(2, n//2+1):
        if n % i == 0:
            yield i
    
    yield n

def gen_triangle(end = -1):
    """Generate triangle numbers: 1 + 2 + 3 + ..."""
    n = 0
    for i in gen_natural_numbers(1, end):
        n += i
        yield n

def gen_factorization(n):
    """Given a number generate the numbers that make up the prime factorization
    of n """

    for p in gen_prime_numbers(int(n ** 0.5)+1):
        if p*p > n: break
        while n % p == 0:
            yield p
            n //= p
    if n > 1: yield n

