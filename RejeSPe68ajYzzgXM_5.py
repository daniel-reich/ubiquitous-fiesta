
def combine(lst):
    res = {}
    for i in lst:
        if i[0] in res:
            res[i[0]].append(i[2])
        else:
            res[i[0]] = [i[2]]
    return res

