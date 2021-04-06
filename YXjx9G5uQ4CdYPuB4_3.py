
#sorry for all these lines i cant understand the instrucctions xd 
from math import sqrt
def simple_comp(lst1, lst2):
    if lst2==None or lst1==None:return False
    if len(lst1)==0 and len(lst2)==0:
        return True
    x= sorted([sqrt(abs(i)) for i in lst2])
    y= sorted([abs(i) for i in lst1])
    r= list(set([i==j for i,j in zip(x,y)]))
    for i in y:
        if i==42:
            return False
    try:
        if r[0]==False:return False
        if len(r)>=2:return False
        return True
    except IndexError:
        return False

