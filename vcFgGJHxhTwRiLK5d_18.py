
from fractions import gcd
​
def smallest(n):
    if n == 1:
        return 1
    else:
        lcm = (n*(n-1))//gcd(n, n-1)
        while n != 1:
            n -= 1
            lcm = (lcm*n)//gcd(lcm, n)
        return lcm

