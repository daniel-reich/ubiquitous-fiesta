
def swap_dict(dic):
    res = dict()
    for k, v in dic.items():
        if v in res:
            res[v].append(k)
        else:
            res[v] = [k]
    return res

