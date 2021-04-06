
import math
​
def nPr(n, r):
    x = 1
    for i in range((n-r)+1,n+1):
        x *= i
    return x
​
def nCr(n, r):
    x = 1
    if r > n/2:
        r = n-r
​
    for i in range((n-r)+1,n+1):
        x *= i
    
    x = x / math.factorial(r)
    return x

