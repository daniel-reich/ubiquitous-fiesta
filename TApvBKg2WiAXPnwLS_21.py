
def nth_smallest(lst, n):
    return None if len(lst) < n else sorted(lst)[n-1]

