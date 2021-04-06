
from collections import Counter
def count_identical_lists(lst1, lst2, lst3, lst4):
    l=[]
    c=0
    l.append(lst1)
    l.append(lst2)
    l.append(lst3)
    l.append(lst4)
    output=Counter([tuple(i) for i in l])
    for i,j in output.items():
        if j>1:
            c=j
    return c

