
def divide(lst, n):
    res = []
    while lst:
        i = 1
        while sum(lst[:i]) <= n and i <= len(lst):
            i += 1
        res.append(lst[:i - 1])
        lst = lst[i - 1:]
    return res

