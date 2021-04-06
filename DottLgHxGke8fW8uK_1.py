
def nPr(n, r):
    res = 1
    for i in range(n - r + 1, n + 1):
        res *= i
    return res
​
​
def nCr(n, r):
    res = 1
    r = min(r, n - r)
    for i in range(n - r + 1, n + 1):
        res *= i
    for i in range(2, r + 1):
        res //= i
    return res

