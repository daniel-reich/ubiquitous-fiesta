
def product_pair(lst, k):
​
    num_1 = 1
    min_num, max_num = 99999, -99999
​
    import itertools
    lst_1 = list(itertools.combinations(lst, k))
​
    if len(lst) < k:
        return None
    else:
        for x in lst_1:
            for y in x:
                num_1 *= y
            if num_1 < min_num:
                min_num = num_1
            if num_1 > max_num:
                max_num = num_1
            num_1 = 1
​
    return (min_num, max_num)

