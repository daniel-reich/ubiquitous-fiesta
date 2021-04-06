
def legendre(p, n):
    i, result = 1, 0
    while p**i<=n:
        result += int(n/(p**i))
        i+=1
    return result

