
def lst_ele_sum(args):
    res =[]
    for i,v in enumerate(args):
        res.append(sum(args[:i])+sum(args[i+1:]))
    return res

