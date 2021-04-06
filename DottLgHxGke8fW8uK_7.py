
import math
def prod(items,start=1):
    for item in items:
        start *= item
    return start
def nPr(n,r):
    return prod(range(n - r + 1, n + 1))
​
def nCr(n, r): 
    p=1
    k=1
    if (n-r<r):
        r=n-r
    if (r != 0):  
        while (r): 
            p *= n 
            k *= r 
            m=gcd(p,k)
            p//=m
            k//=m
            n-=1
            r-=1
    else:
        p=1
    return p    
def gcd(a,b):
    if (b == 0): 
         return a 
    return gcd(b, a%b)

