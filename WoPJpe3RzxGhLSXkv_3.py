
def concatenation_sum(n):
    s = 0
    if n < 10:
        return n
    else:
        x = 9
        while n > 0:
            if x < n:
                n = n - x
                s += x * len(str(x))
            else:
                s += n * len(str(x))
                n = 0
            x *= 10
    return s

