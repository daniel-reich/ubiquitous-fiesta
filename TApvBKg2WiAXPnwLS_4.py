
def nth_smallest(lst, n):
    try:
        return sorted(lst)[n-1]
    except IndexError:
        return None

