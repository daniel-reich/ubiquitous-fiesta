
def group(lst, size):
    s=len(lst)/size
    if s%1!=0:s=s+1
    a=int(s)
    print(a)
    l=[]
    for x in range(0,a):
     l.append(lst[x::a])
    return [x for x in l if x!=[]]

