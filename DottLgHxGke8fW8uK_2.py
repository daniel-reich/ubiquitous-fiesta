
from math import factorial
​
def nCr(n, r):
    total = 1
    for i in range(min(r, n-r)):
        total = total * (n-i) // (i+1)
    return total
​
def nPr(n, r):
    return nCr(n, r) * factorial(r)

