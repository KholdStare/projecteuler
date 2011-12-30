#!/usr/bin/python
# allow importing from utils
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from seriesutils import *

def main(number):
    sum_squares = partial_sum_squares(number)
    square_sum = partial_sum(number) ** 2
    return square_sum - sum_squares

if __name__ == "__main__":
    print main(100)
