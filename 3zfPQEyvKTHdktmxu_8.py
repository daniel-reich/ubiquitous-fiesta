
def big_sub(lst):
    n = len(lst)
    res = [lst[0], 0, 0]
    for r in range(n):
        if lst[r] > 0:
            s = lst[r]
            if s >= res[0]:
                res = [s, r, r]
            for c in range(r + 1, n):
                s += lst[c]
                if s >= res[0]:
                    res = [s, r, c]
    return res

