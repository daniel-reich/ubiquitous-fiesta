
from math import log
def maya_number(n):
    if n==0:return ['@']
    m=[]
    for a in range(int(log(n)//log(20)),-1,-1):
        q=n//20**a
        if q>=1:
            lines=q//5
            dots=q%5
            m.append('o'*dots+'-'*lines)
            n-=q*20**a
        else:
            m.append('@')   
    return m

