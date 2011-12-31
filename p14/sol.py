#!/usr/bin/python

def problem_rule(n):
    if n <= 1:
        return None
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def count_sequence_steps(n, rule):
    count = 0
    while n is not None:
        n = rule(n)
        count += 1

    return count

def main (limit):
    maxCount = 1
    maxN = 1
    
    for n in xrange(1, int(limit)):
        print n
        count = count_sequence_steps(n, problem_rule) 
        if count > maxCount:
            maxCount = count
            maxN = n

    return maxN


if __name__ == "__main__":
    print main(1e6)
