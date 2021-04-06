
from math import log10
def concatenation_sum(n):
    if n<10:return n
    a=int(log10(n))+1
    return sum(i*int('9'+'0'*(i-1)) for i in range(1,a))+(a)*(n-int('9'*(a-1)))

