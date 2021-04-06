
def less_or_equal(lst, k):
    lst.sort()
    if k == 0 and 1 not in lst:
        return 1
    elif len(lst) == k:
        return lst[k - 1]
    elif len(lst) > k and lst[k - 1] != lst[k]:
        return lst[k - 1]

