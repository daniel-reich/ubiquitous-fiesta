
def relation_lst(lst):
    lst.sort()
    res =[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            res.append((lst[i],lst[j]))
    return res

