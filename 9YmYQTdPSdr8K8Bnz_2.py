
def unique_lst(lst):
    newlst = []
    for l in lst:
        if l > 0 and l not in  newlst:
            newlst.append(l)
    return newlst

