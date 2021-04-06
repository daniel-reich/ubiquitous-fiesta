
def nPr(n, r):
    s = 1
    for i in range(n-r+1, n+1):
        s *= i
    return s
​
​
def nCr(n, r):
    if r > n - r:
        r = n - r
    s = 1
    for i in range(1, r+1):
        s *= n - r + i
        s //= i
    return s

