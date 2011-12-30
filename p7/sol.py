#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from numutils import gen_prime_numbers

def main (n):
    i = 0
    prime = 0
    for p in gen_prime_numbers():
        i+=1
        prime = p
        if i >= n:
            break

    return prime

if __name__ == "__main__":
    print main(10001)
