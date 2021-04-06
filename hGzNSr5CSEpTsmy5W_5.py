
def not_good_math(n, k):
    while k:
        r = n % 10
        if r:
            if k >= r:
                k -= r
                n -= r
            else:
                n -= k
                k = 0
        else:
            n //= 10
            k -= 1
    return n

