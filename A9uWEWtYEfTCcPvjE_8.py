
from itertools import combinations
def price_importance_sort(d, b):
    lst = []
    for k, val in d.items():
        sub_lst = [val['price'], val['importance'], k]
        lst.append(sub_lst)
    lst_fit = []
    for n in range(len(lst), 0, -1):
        for comb in combinations(lst, n):
            total_p = 0
            total_i = 0
            for item in comb:
                total_p += item[0]
                total_i += item[1]
            if total_p <= b:
                lst_fit.append((total_i, total_p, list(comb)))
    lst_fit.sort(key=lambda x: (-x[0], x[1]))
    if lst_fit[0][0] == lst_fit[1][0]:
        print('tie')
    res = [sub_lst[2] for sub_lst in lst_fit[0][2]]
    return sorted(res)

