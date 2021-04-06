
import math
def simple_comp(lst1,lst2):
    if lst2 == None or lst1 == None:
        return False
    x = [x*x for x in lst1]
    count = 0
    print(x)
    print(lst2)
    for eachnumber in x:
        if x.count(eachnumber) == lst2.count(eachnumber):
            continue
        else:
            return False
    for eachnumber in lst2:
        if eachnumber not in x:
            return False
    return True

