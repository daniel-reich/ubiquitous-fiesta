
from itertools import groupby
def look_and_say(start, n):
    res,list1=[],list(str(start))
    #list1=list(str(start))
    res.append(start)
    for i in range(n-1): 
        count_dups = "".join(["".join((str(len(list(val))),str(key))) for key,val  in groupby(list1)])
        list1=list(str(count_dups))
        res.append(int(count_dups))
    return res

