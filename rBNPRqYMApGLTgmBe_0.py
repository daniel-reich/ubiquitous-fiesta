
def combinations(k, n):
    ways = 1
    for i in range(min(k, n-k)):
        ways = ways * (n-i) // (i+1)
    return ways

