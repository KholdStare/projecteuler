
def binary_search(val, lst, s, e):
    """Given sorted list in ascending order lst, and starting/ending indeces (inclusive),
    return index where value should be."""

    if val > lst[e] or val < lst[s]:
        return -1
    
    while s < e:
        half = (s+e) // 2
        if val == lst[half]:
            return half
        elif val < lst[half]:
            e = half - 1
        else:
            s = half + 1

    if lst[e] == val:
        return e

    return -1
