
from functools import  reduce
def digital_division(n):
    l = list(map(lambda x:int(x),str(n)))
    t1 = reduce(lambda a,b:a*b,l)
    t1 = n%t1==0 if t1!=0 else False
    t2 = n%reduce(lambda a,b:a+b,l)==0
    t2 = n % t2 == 0 if t2 != 0 else False
    t3=True
    for i in l:
        if i==0:continue
        if n%i!=0:
            t3=False
            break
    ans = [t1,t2,t3].count(True)
    return "Perfect" if ans==3 else "Indivisible" if ans==0 else ans

