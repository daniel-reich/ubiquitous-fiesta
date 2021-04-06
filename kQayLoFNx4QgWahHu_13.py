
def order(lst):
    r = []
    o_lst = sorted(lst.copy())
    for i in o_lst:
        r.append(lst.index(i))
        lst[lst.index(i)] = "_"
    return r

