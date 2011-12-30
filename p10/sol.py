#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import gen_prime_numbers

def main (n):
    s = 0
    for p in gen_prime_numbers(n):
        s += p

    return s

if __name__ == "__main__":
    print main(2e6)
