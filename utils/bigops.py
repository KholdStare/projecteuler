# module for operations on lists of digits. Allows arbitrary precision arithmetic
# currently only integers

# conversions
def int_to_list(n):
    return [ int(d) for d in list(str(n)) ]

def list_to_int(l):
    """Caution, number represent by list of digits might be too big to be represented."""
    return int("".join([ str(d) for d in l ]))

def list_to_str(l):
    return "".join([ str(d) for d in l ])

    

# operations
def _mul_gen_summands(acc, num):
    """Given two big numbers to multiply, generates summands for the multiplication."""
    if len(acc) >= len(num):
        a = acc
        b = num
    else:
        a = num
        b = acc
    aLen = len(a)
    bLen = len(b)

    # for each digit of b multiply by a to generate a summand
    for i in xrange(0, bLen):
        summand = [ b[bLen-1-i] * d for d in a ]
        summand.extend([0] * i)
        yield summand

def mul(acc, num):
    return sum_sequence(_mul_gen_summands(acc, num))

def mul_sequence(numSequence):
    # Start off with first element as accumulator
    if isinstance(numSequence, list):
        if len(numSequence) == 0:
            return [1]
        acc = numSequence.pop(0)
    else:
        acc = numSequence.next()
        if acc is None:
            return [1]

    acc = reduce(mul, numSequence, acc)

    return acc

def add_no_carry(acc, num):
    # add a and b where a is at least as long as b
    # acc stores the result in 
    if len(acc) >= len(num):
        a = acc
        b = num
    else:
        a = num
        b = acc
    aLen = len(a)
    bLen = len(b)

    for i in xrange(0, aLen):
        a[-1-i] += (b[-1-i] if i<bLen else 0)

    return a

def resolve_carries(a):
    aLen = len(a)
    carry = 0
    for i in xrange(-1, -1-aLen, -1):
        columnSum = a[i] + carry
        carry = columnSum // 10
        a[i] = columnSum % 10

    while carry > 0:
        a.insert(0, carry % 10)
        carry //= 10


def add(acc, num):
    carry = 0

    # add a and b where a is at least as long as b
    # acc stores the result in 
    if len(acc) >= len(num):
        a = acc
        b = num
    else:
        a = num
        b = acc
    aLen = len(a)
    bLen = len(b)

    for i in xrange(0, aLen):
        columnSum = a[-1-i] + (b[-1-i] if i<bLen else 0) + carry
        carry = columnSum // 10
        a[-1-i] = columnSum % 10

    while carry > 0:
        a.insert(0, carry % 10)
        carry //= 10

    return a


def sum_sequence(numSequence):
    # Start off with first element as accumulator
    if isinstance(numSequence, list):
        if len(numSequence) == 0:
            return [0]
        acc = numSequence.pop(0)
    else:
        acc = numSequence.next()
        if acc is None:
            return [0]

    acc = reduce(add_no_carry, numSequence, acc)
    resolve_carries(acc)

    return acc
