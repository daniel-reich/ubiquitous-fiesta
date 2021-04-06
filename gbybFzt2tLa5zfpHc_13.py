
from itertools import combinations
​
​
def three_sum(lst):
    if len(lst) < 3:
        return []
    res = []
    for tpl in combinations(lst, 3):
        lst_tpl = list(tpl)
        if sum(lst_tpl) == 0:
            if lst_tpl not in res:
                res.append(lst_tpl)
    return res

