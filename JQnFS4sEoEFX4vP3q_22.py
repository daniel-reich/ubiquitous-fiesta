
from itertools import combinations
​
​
def product_pair(lst, k):
    if k > len(lst):
        return None
    if k == 1:
        sort_lst = sorted(lst)
        return (sort_lst[0], sort_lst[-1])
    total_lst = list(combinations(lst, k))
    res = sorted([lst_mul(i) for i in total_lst])
    return (res[0], res[-1])
​
​
def lst_mul(lst):
    sum_to = 1
    for i in lst:
        sum_to *= i
    return sum_to

