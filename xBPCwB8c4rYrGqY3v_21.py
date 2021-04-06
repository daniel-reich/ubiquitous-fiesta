
from collections import Counter
​
def missing(lst):
    C = Counter([lst[k] - lst[k-1] for k in range(1, len(lst))])
    diff = [k for k,v in C.items() if v > 0][0]
    last = lst[0]
    for cur in lst[1:]:
        if cur - last != diff:
            return last + diff
        last = cur

