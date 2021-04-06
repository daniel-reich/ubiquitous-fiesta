
def num_in_str(lst):
    res = []
    for i in lst:
        for j in i:
            if j.isdigit():
                res.append(i)
                break
    return res

