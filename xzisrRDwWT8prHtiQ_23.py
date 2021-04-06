
def difference_two(lst):
    res =[]
    for x in lst:
        for y in lst:
            if (x-y)==-2:res.append([x,y])
    return sorted(res,key=lambda x:x[0])

