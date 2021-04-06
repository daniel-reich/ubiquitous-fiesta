
from itertools import *
​
def get_subsets(lst, n):
    comb = []
    for i in range(1, len(lst) + 1):
        comb.append(list([list(x) for x in combinations([x for x in range(len(lst))], i)]))
    return [[lst[i] for i in j] for k in comb for j in k if sum([lst[i] for i in j]) == n]

