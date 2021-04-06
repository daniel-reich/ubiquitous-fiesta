
def func_sort(lst):
    d = dict()
    for i in range(len(lst)):
        d[i] = 0
        f = lst[i]
        while callable(f) is True:
            d[i] += 1
            f = f()
    return sorted(lst, key=lambda x:d[lst.index(x)])

