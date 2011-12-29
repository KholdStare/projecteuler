#!/usr/bin/python

limit = 4e6

# use generator
def gen_fibonacci():
    a = 0
    b = 1
    while 1 == 1:
        c = a + b
        yield c
        a = b
        b = c

result = 0
for f in gen_fibonacci():
    if f > limit:
        break

    if f % 2 == 0:
        result += f

print result

