
from itertools import combinations
​
​
def get_subsets(lst, n):
    res = []
    for num in range(1, len(lst) + 1):
        num_lst = []
        for comb in combinations(lst, num):
            if sum(comb) == n:
                num_lst.append(sorted(list(comb)))
        res += sorted(num_lst)
    return res

