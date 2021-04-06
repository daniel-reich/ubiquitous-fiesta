
import math 
def prime_factors(n):
    pfLst=[]
    while n % 2 == 0: 
        pfLst.append(2)
        n = n / 2
​
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            pfLst.append(i)
            n = n / i
    if n>2:
        pfLst.append(int(n))
    return pfLst

