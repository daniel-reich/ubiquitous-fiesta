
from math import log
def base_n(base, values, num):
    if len(values)!=base:
        return False
    n=int(log(num)/log(base))
    ans=''
    for a in range(n,-1,-1):
        index=int(num/base**a)
        ans+=str(values[index])
        num=num%(base**a)
    return ans

