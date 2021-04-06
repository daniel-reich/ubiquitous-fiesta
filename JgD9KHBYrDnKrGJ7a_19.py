
def swap_dict(dic):
    res = {}
    for v, k in dic.items():
        if k in res:
            res[k].append(v)
        else:
            res[k] = [v]
    return res

