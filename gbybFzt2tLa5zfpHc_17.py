
from itertools import combinations
​
​
def three_sum(lst):
    l = list(combinations(lst, 3))
    arr = []
    for i in l:
        if sum(i) == 0 and list(i) not in arr:
            arr.append(list(i))
​
    return arr

