
import itertools as it
​
def repeat(lst, n):
    lst[:] = list(it.chain.from_iterable(it.repeat(lst,n)))
    return lst
​
def add(lst, x):
    lst.append(x)
    return lst    
​
def remove(lst, i, j):
    if i > len(lst) or i > j or i < 0:
        return lst
    if j >= len(lst):
        lst[i:] = []
    else:
        lst[i:j+1] = []
    return lst
​
def concat(lst, lst2):
    lst += lst2
    return lst

