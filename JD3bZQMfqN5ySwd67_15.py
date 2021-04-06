
from functools import reduce
from math import ceil, floor
​
def permuta(lst, step=0):
    if step==len(lst):
        return lst
    flst = []
    nlst = lst.copy()
    for i in range(step, len(nlst)):
        nlst[step],nlst[i] = nlst[i],nlst[step]
        b = list(permuta(nlst, step+1))
        if type(b)==list and type(b[0])==tuple:
            flst += b
        else:
            flst.append(b)
    flst = list(map(tuple, flst))
    return set(flst)
​
def p2(lst):
    lst = list(lst)
    if len(lst[0])%2==0:
        k = len(lst[0])//2
        nlst = [("".join(lst[i][:k]),"".join(lst[i][k:])) for i in range(len(lst))]
        return nlst
    else:
        top = ceil(len(lst[0])/2)
        btm = floor(len(lst[0])/2)
        nlst = [("".join(lst[i][:top]),"".join(lst[i][top:])) for i in range(len(lst))]
        nlst += [("".join(lst[i][:btm]),"".join(lst[i][btm:])) for i in range(len(lst))]
        return nlst
        
def is_vampire(number):
    if len(str(number))==1:
        return "Normal Number"
    lnum = [a for a in str(number)]
    ncomb = list(permuta(lnum))
    ncomb = p2(ncomb)
    for i in range(len(ncomb)):
        ncomb[i] = tuple(map(int, ncomb[i]))
    cv = checker(ncomb, number) 
    if cv == False:
        return "Normal Number"
    elif len(str(number))%2==0:
        return "True Vampire"
    else:
        return "Pseudovampire"
​
def checker(lst, number):
    if len(lst)==1:
        a = reduce(lambda x,y: x*y, lst[0])
        return a==number
    a = reduce(lambda x,y: x*y, lst[0])
    return a==number or checker(lst[1:], number)

