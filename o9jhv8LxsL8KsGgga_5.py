
def bound_sort(lst, b):
    pre = lst[b[0]:b[1]+1]
    suff = lst[b[1]+1:]
    return sorted(pre) + suff == sorted(lst)

