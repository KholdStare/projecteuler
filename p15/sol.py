#!/usr/bin/python
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from decoratorutils import memoized

@memoized
def main (m, n):
    if m==0 and n==0:
        return 1

    count = 0
    if m > 0:
        count += main(m-1, n)
    
    if n > 0:
        count += main(m, n-1)

    return count


if __name__ == "__main__":
    print main(20, 20)
