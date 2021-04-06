
from fractions import Fraction
​
​
def farey(n):
    return ['0/1']+list(map(lambda x: '1/1' if x == 1 else str(x), sorted ({Fraction(num,denom) for num in range (1,n+1) for denom in range(num,n+1)})))

