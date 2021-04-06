
def duplicate_nums(lst):
    newlst = []
    for x in lst:
        if lst.count(x) > 1:
            newlst.append(x)
    if set(newlst):
        return sorted(list(set(newlst)))
    else:
        return None

