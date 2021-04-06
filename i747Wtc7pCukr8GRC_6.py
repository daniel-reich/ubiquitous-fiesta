
import itertools
def mult(j):
    h = 1
    for i in j:
        h=h*i
    return h
def max_product(lst):
    l = []
    for i in range(len(lst)+1):
        for j in itertools.combinations(lst,i):
            if len(j)==3:l.append(mult(list(j)))
    return max(l)
def min_product(lst):
    l = []
    for i in range(len(lst)+1):
        for j in itertools.combinations(lst,i):
            if len(j)==3:l.append(mult(list(j)))
    return min(l)

