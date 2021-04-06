
def combinations(k, n):
    if n==k: return 1
    prod = lambda s, e: e if s == e else s * prod(s-1, e)
    return prod(n, 1 + max(k, n-k)) // prod(min(k, n-k), 1)

