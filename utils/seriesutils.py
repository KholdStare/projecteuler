def sum_consecutive_nums(k, n):
    return (n-k+1)*(n+k) / 2

def partial_sum(n):
    return n * (n+1) / 2

def partial_sum_squares(n):
    return n * (n+1) * (2*n + 1) / 6

def sum_consecutive_squares(k, n):
    return partial_sum_squares(n) - partial_sum_squares(k-1)
