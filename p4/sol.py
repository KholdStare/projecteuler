#!/usr/bin/python

def is_palindrome(a):
    return str(a) == str(a)[::-1]

def main(digits):
    maxNum = (10 ** digits) - 1
    leastNum = 10 ** (digits - 1)
    largestPalindrome = 0

    for a in xrange(maxNum, leastNum, -1):
        for b in xrange(maxNum, leastNum, -1):
            num = a * b
            if is_palindrome(num) and num > largestPalindrome:
                largestPalindrome = num

    return largestPalindrome

if __name__ == "__main__":
    print main(3)
