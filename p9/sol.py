#!/usr/bin/python

def multof3or5(num):
    return num % 3 == 0 or num % 5 == 0

def main(totalSum):
    for a in xrange(0, totalSum-1):
        for b in xrange(a+1, totalSum):
            c2 = a**2 + b**2
            c = c2 ** 0.5
            if c <= b or int(c) != c:
                continue
            c = int(c)
            if a+b+c == totalSum:
                return a*b*c

    return 0


if __name__ == "__main__":
    print main(1000)
