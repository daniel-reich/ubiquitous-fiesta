
import math
def sum_d(n):
    if n<10:
        return n*(n+1)//2
    d=int(math.log10(n))
    p=pow(10,d)
    msd=n//p
    return (msd*45*d*pow(10,d-1))+(msd*(msd-1)//2*p)+(msd*(1+n%p)+sum_d(n%p))
​
def digits_sum(start, stop):
  return sum_d(stop)-sum_d(start-1)

