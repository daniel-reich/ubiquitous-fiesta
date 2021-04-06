
from itertools import permutations
def next_number(num):
    lst=[]
    num1=list(map(str,str(num)))
    if len(num1)==1:
        return num
    elif num1[::-1]==sorted(num1):
        return num
    else:
        for i in list(permutations(num1)):
            lst.append(int("".join(i)))
        lst=list(set(lst))
        lst=sorted(lst)
    a=lst.index(num)
    return lst[a+1]

