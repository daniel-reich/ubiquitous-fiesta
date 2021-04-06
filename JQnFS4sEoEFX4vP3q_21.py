
from itertools import combinations
​
​
def product_pair(lst, k):
    if k>len(lst):
        return None
    a,c = list(combinations(lst, k)),[]
    for i in range(len(a)):
        b = 1
        for j in a[i]:
            b *= j
        c.append(b)
    return min(c), max(c)

