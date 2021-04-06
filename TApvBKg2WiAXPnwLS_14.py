
def nth_smallest(lst, n):
    lst.sort()
    l = len(lst)
    if n <= l:
        return lst[n - 1]
    else:
        return None

