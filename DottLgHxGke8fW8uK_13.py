
from math import factorial as f
def nPr(n, r):
    a = n
    i = n-1
    while i>(n-r):
        a*=i
        i-=1
​
    return(a)
​
def nCr(n, r):
    a = 1
    i = n
    if (n-r)>r:
        while i>(n-r):
            a*=i
            i-=1
        return a/f(r)
    else:
        while i>r:
            a*=i
            i-=1
        return a/f(n-r)

