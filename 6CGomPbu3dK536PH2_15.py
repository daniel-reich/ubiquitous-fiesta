
def accumulating_list(lst):
    relst=[]
    for i in range(1,len(lst)+1):
        relst.append(sum(lst[:i]))
    return relst

