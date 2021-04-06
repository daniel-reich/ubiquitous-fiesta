
def rotate_transform(l,n):
    l2=[]
    if n >= 0:
        for z in range(n):
            for x in range(len(l)):
                l1=[]
                for y in range(len(l[x])-1,-1,-1):
                    l1.append(l[y][x])
                l2.append(l1)
            l=l2
            l2=[]
        return l
    else:
        for z in range(n,0,1):
            for x in range(len(l)-1,-1,-1):
                l1=[]
                for y in range(len(l[x])):
                    l1.append(l[y][x])
                l2.append(l1)
            l=l2
            l2=[]
        return l

