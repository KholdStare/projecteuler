
def is_prime(a, primes):
    """ Returns true if number is a prime. Relies on a set of primes,
    and thus needs to be called on numbers in order."""
    if len(primes) == 0:
        return True

    for p in primes:
        if a % p == 0:
            return False

    return True
