#!/usr/bin/python

def multof3or5(num):
    return num % 3 == 0 or num % 5 == 0

def main(limit):
    result = 0
    for num in range(1,limit):
        if multof3or5(num):
            result += num

    return result

if __name__ == "__main__":
    print main(1000)
