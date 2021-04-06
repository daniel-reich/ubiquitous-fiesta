
def legendre(p, n):
    i = 1
    result = 0
    while p**i <= n:
        result = result + (n//p**i)
        i += 1
    return result

