
def leader(lst):
    res = lst[-1:]
    for v in lst[:-1][::-1]:
        if all(v > x for x in res):
            res.append(v)
    return res[::-1]

