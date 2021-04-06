
import itertools
def coins_div(lst):
    s = sum(lst)/3
    if s==1:return True
    l=[]
    for i in range(1,7):
       for j in itertools.combinations(lst,i):
           if sum(list(j))==s and j not in l:l.append(j)
    l2 = [y for x in l for y in x]
    for i in lst:
        if i not in l2:return False
​
    return True

