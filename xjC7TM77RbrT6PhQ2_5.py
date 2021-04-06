
def switches(n, s = 0):
    while n > 0:
        s, n = s + 2**(n-1), n - 2
    return s

