
from operator import xor
def boolean_and(lst):
    a = lst[0]
    for i in range(1, len(lst)):
        a = (a and lst[i])
    return a
​
​
def boolean_or(lst):
    a = lst[0]
    for i in range(1, len(lst)):
        a = (a or lst[i])
​
    return a
​
​
​
​
​
def boolean_xor(lst):
    a = lst[0]
    for i in range(1, len(lst)):
        a = xor(a,lst[i])
​
    return a

