
from itertools import combinations as combo
def coins_div(lst):
    k=0
    if 0 in lst:
        lst.remove(0)
    lng=len(lst)
    a=sum(lst)/3
    if lst==[a,a,a]:
        return True
    if len(lst)<3 or a-int(a)!=0 or max(lst)>a:
        return False
    for i in range(1,len(lst)-2,1):
        c=combo(lst,i)
        for i in c:
            if sum(i)==a:
                k+=1
                temp=lst.copy()
                for j in i:
                    if j in lst:
                        lst.remove(j)
                    else:
                        lst=temp
                        k-=1
                        break
                if k==3 and lst==[]:
                    return True
    return False

