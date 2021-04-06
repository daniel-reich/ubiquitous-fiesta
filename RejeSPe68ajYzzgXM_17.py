
def combine(lst):
    res = dict()
    for i in lst:
        if i[0] not in res:
            res[i[0]] = ['Sx', 'Sx']
        res[i[0]][i[1]] = i[2]
    return res

