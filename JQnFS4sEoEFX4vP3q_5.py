
from functools import reduce
def product_pair(lst, k):
    len_lst = len(lst)
    if len_lst < k:
        return None
    elif len_lst == k:
        res = reduce(lambda a, b: a * b, lst)
        return res, res
    elif k == 1:
        return min(lst), max(lst)
    lst.sort(key=lambda x: abs(x), reverse=True)
    prod_k = reduce(lambda a, b: a * b, lst[:k])
    if prod_k > 0:
        res_max = prod_k
        positive_k1 = lst[k - 1] > 0
        for i in range(k, len_lst):
            if positive_k1 and lst[i] <= 0:
                res = reduce(lambda a, b: a * b, lst[:k - 1]) * lst[i]
                return res, res_max
            elif not positive_k1 and lst[i] >= 0:
                res = reduce(lambda a, b: a * b, lst[:k - 1]) * lst[i]
                return res, res_max
        res_min = reduce(lambda a, b: a * b, lst[-k:])
        return res_min, res_max
    elif prod_k < 0:
        res_min = prod_k
        positive_k1 = lst[k - 1] > 0
        for i in range(k, len_lst):
            if positive_k1 and lst[i] <= 0:
                res = reduce(lambda a, b: a * b, lst[:k - 1]) * lst[i]
                return res_min, res
            elif not positive_k1 and lst[i] >= 0:
                res = reduce(lambda a, b: a * b, lst[:k - 1]) * lst[i]
                return res_min, res
        res_max = reduce(lambda a, b: a * b, lst[-k:])
        return res_min, res_max
    return 0, 0

