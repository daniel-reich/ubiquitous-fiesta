
def super_digit(n, k):
    n = sum(int(d) for d in str(n)) * k
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

