
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
    while end < 0 or i <= end:
        yield i
        i += incr

def gen_prime_numbers(end = -1):
    """Generates prime numbers."""
    yield 2
    yield 3
    prime_list = [2, 3]
    for n in gen_natural_numbers(5, end, 2):
        if is_prime(n, prime_list):
            prime_list.append(n)
            yield n
                

def gen_factorization(n):
    """Given a number, generate the numbers that make up the prime factorization
    of n """
    factorization = []

    for p in gen_prime_numbers(int(n ** 0.5)+1):
        if p*p > n: break
        while n % p == 0:
            yield p
            n //= p
    if n > 1: yield n

