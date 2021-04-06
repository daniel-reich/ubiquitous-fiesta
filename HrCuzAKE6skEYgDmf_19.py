
from math import ceil
def pairs(lst):
    lists = [[] for i in range(ceil(len(lst)/2))]
    for j in range(ceil(len(lst)/2)):
        lists[j].append(lst[j]) ; lists[j].append(lst[len(lst) - 1 - j])
    return lists

