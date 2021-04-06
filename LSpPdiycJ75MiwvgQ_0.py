
def grid_pos(lst):
    lst.sort()
    res = 1
    for k in range(lst[1] + 1, sum(lst) + 1):
        res *= k
    for k in range(2, lst[0] + 1):
        res //= k
    return res

