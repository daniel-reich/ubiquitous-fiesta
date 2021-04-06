
def eratosthenes(n):
    return [x for x in range(2, n+1) if all(x % y for y in range(2, x))]

