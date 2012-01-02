#!/usr/bin/python

import math

def sum_of_digits_factorial(n):
    s = 0
    while n > 0:
        s += math.factorial(n % 10)
        n = n // 10

    return s

def gen_special_nums():
    # find bound
    maxNum = 7 * math.factorial(9)
    for n in xrange(10, maxNum+1):
        if n == int(sum_of_digits_factorial(n)):
            yield n

def main ():
    return sum( gen_special_nums() )

if __name__ == "__main__":
    print main()
