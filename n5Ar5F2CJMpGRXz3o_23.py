
def mineral_formation(cave):
    a=[]
    b=[]
    a.append(cave[0])
    b.append(cave[-1])
    if sum(a[0])==0:
        return "stalagmites"
    elif sum(b[0])==0:
        return "stalactites"
    elif sum(a[0])>0:
        return  "both"

