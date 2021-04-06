
import math
​
def find_median(lst):
    if len(lst) % 2 == 0:  # even
        return (lst[int(len(lst)/2)]+lst[int(len(lst)/2-1)])/2
    else:  # odd
        return lst[math.ceil(len(lst) / 2) - 1]
​
def iqr(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 0:  # even
        median = int(len(lst) / 2)
        upper = lst[median:]
        lower = lst[:median]
    else: #odd
        median = math.ceil(len(lst) / 2)
        upper = lst[median:]
        lower = lst[:median - 1]
    Q1 = find_median(lower)
    Q3 = find_median(upper)
    return Q3 - Q1

