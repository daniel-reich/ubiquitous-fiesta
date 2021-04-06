
import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
​
def dice_roll(n, l):
    sum1=0
    l=l-n
    for i in range(n+1):
        if l-6*i+n-1<=0 or l-6*i+n-1<n-1:
            break
        sum1+=(-1)**i*nCr(n,i)*nCr(l-6*i+n-1,n-1)
    return int(sum1)

