
def sums_up(lst):
    res = []
    for idx, i in enumerate(lst):
        if 8 - i in lst[:idx]:
            res.append(sorted((8-i, i)))
    return {'pairs': res}

