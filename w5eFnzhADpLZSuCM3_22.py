
def multiplicity(arr):
    temp_list = [[x, arr.count(x)] for x in arr]
    res = []
    for elem in temp_list:
        if elem not in res:
            res.append(elem)
    return res

