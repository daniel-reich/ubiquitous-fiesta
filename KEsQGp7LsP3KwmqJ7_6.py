
def check(lst):
    sorted_lst = sorted(lst)
    if lst == sorted_lst:
        return 'NO'
    start = lst.index(min(lst))
    rotated = lst[start:] + lst[:start]
    return 'YES' if rotated == sorted_lst else 'NO'

