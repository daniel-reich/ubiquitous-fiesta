
import math
​
def nPr(n, r):
    return nCr(n, r) * math.factorial(r)
​
def nCr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    res = 1
    for k in range(1,r + 1):
        res = res * (n - k + 1) // k
    return res

