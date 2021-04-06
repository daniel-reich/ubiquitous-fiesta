
from itertools import product
def unravel(txt):
    lst=[]
    i=0
    while(i<len(txt)):
        if txt[i] == '[':
            tmp=""
            i+=1
            while(txt[i]!=']'):
                tmp=tmp+txt[i]
                i+=1 
            lst.append(tmp.split("|"))
        else:
            lst.append(list(txt[i]))
        i+=1
    res=lst[0]
    for x in lst[1:]:
        res=list(product(res,x))
        res=["".join(x) for x in res]
    return sorted(res)

