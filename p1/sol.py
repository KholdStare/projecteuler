#!/usr/bin/python

limit = 1000

def multof3or5(num):
    return num % 3 == 0 or num % 5 == 0

result = 0
for num in range(1,limit):
    if multof3or5(num):
        result += num

print result
