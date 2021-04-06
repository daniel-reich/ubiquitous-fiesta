
def min_miss_pos(lst=list):
    somelist=[]
    lst=sorted(lst)
    fkedup=[]
    for x in lst:
        if x not in somelist:
            somelist.append(x)
​
    for x in range(len(somelist)-1):
        if somelist[x]==somelist[x+1]-1:
            continue
        else:
            if somelist[x]+1==0:
                continue
            if somelist[x]+1<0:
                continue
            else:
                fkedup.append(somelist[x]+1)
    if fkedup == []:
        return somelist[-1]+1
    return min(fkedup)

