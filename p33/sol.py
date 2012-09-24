#!/usr/bin/env python
import fractions

# use a tuple to represent a fraction

def gen_two_digit():
    return (n for n in xrange(11, 100) if ( n%10 != 0 ) )

def share_digit(a, b):
    """Return a digit shared by both numbers.
    If no digit, shared, return 0
    """

    strA = str(a)
    strB = str(b)

    digit = strA[0]

    if strB.find(digit) != -1:
        return int( digit )

    digit = strA[1]

    if strB.find(digit) != -1:
        return int( digit )

    return 0

def remove_digit(num, digit):
    """Given a number, and a digit, return the number with that digit
    removed.
    """

    strNum = str(num)
    strDigit = str(digit)
    i = strNum.find(strDigit)

    if i < 0:
        return num

    return int(strNum[i-1]) # a bit of a hack to get the other digit


def main():
    fracs = get_curious_fractions()

    result = reduce(lambda s, t: (s[0]*t[0], s[1]*t[1]), fracs)
    gcd = fractions.gcd(result[0], result[1])
    return result[1]/gcd

def get_curious_fractions():
    result = []

    for num in (n for n in xrange(11, 100) if (n%10 != 0) ):
        for denom in (m for m in xrange(num+1, 100) if (m%10 != 0) ):
            digit = share_digit(num, denom)

            if (digit == 0):
                continue

            strippedNum = remove_digit(num, digit)
            strippedDenom = remove_digit(denom, digit)

            if ( strippedNum == strippedDenom ):
                continue

            if ( float(num*strippedDenom) / strippedNum ) == denom:
                result.append( (num, denom) )

    return result
    

if __name__ == "__main__":
    print main()

