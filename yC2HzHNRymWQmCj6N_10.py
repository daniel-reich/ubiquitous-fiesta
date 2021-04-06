
def less_or_equal(lst, k):
    lst.sort()
    if k == 0:
        return 1 if lst[0] > 1 else None
    if k > len(lst):
        return
    if k == len(lst):
        return lst[-1]
    return lst[k-1] if lst[k] != lst[k-1] else None

