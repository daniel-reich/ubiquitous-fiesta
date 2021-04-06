
import math
def numberSequence(n):
    res=[]
    if n<=0:
        return '-1'
    else:
        if n%2!=0:
            n=math.ceil(n/2)
            x=[str(i) for i in range(1,n+1)]
            a=x[::-1]+x[1:]
            b=[str(x) for x in a] 
            return str(" ".join(b))
        if n%2==0:
            n=math.ceil(n/2)
            x=[str(i) for i in range(1,n+1)]
            a=x[::-1]+x
            b=[str(x) for x in a] 
            return str(" ".join(b))

