
def antipodes_average(lst):
    sep = int(len(lst)/2 - 1)
    if len(lst)%2==0 :
        return [(i+j)/2 for i, j in zip(list(lst[0:sep+1]), list(lst[sep+1:])[::-1])]
    num = int(len(lst)/2)
    lst.remove(lst[num])
    return antipodes_average(lst)

