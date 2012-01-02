#!/usr/bin/python

def get_sorted_digits(n):
    return "".join(sorted(list(str(n))))

def main (maxMult):

    for n in xrange(1, int(1e10)):
        digits = get_sorted_digits(n)
        success = True
        for mult in xrange(2, maxMult+1):
            if digits != get_sorted_digits(mult*n):
                success = False
                break

        if success:
            return n


if __name__ == "__main__":
    print main(6)
