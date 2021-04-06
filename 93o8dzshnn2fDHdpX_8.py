
def lst_ele_sum(lst):
    newlst = []
    for x in range(len(lst)):
        add = sum(lst[x+1:] + lst[:x])
        newlst.append(add)
    return newlst

