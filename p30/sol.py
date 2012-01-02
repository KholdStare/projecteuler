#!/usr/bin/python

def sum_of_digits_to_power(n, p):
    s = 0
    while n > 0:
        s += (n % 10) ** p
        n = n // 10

    return s

def gen_special_nums(power):
    maxNum = (power+1) * (9 ** power)
    for n in xrange(2, maxNum+1):
        if n == int(sum_of_digits_to_power(n, power)):
            yield n

def main (power):
    return sum( gen_special_nums(power) )

if __name__ == "__main__":
    print main(5)
