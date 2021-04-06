
def sum_of_slices(lst):
    if lst[0] > 100:
        res = [0, lst[0]]
        lst = lst[1:]
    else:
        res = []
    while sum(lst) > 100:
        while lst and lst[0] >= 100:
            res.append(lst[0])
            lst = lst[1:]
        if not lst:
            break
        i = 1
        while sum(lst[:i]) < 100:
            i += 1
        res.append(sum(lst[: i - 1]))
        lst = lst[i - 1:]
    if lst:
        res.append(sum(lst))
    return res

