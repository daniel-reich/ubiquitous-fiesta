
def asc(c):
    res=0
    for i in c:
        res+=ord(i)
    return res    
def pairwise_swap(lst):
    x,y=[],[]
    if len(lst)%2==0:
        return [lst[i^1] for i in range(len(lst))]
    if len(([i for i in lst if type(i)==int]))==len(lst):
        z=[lst[i^1] for i in range(len(lst[0:-1]))]
        if asc(str(lst[-1]))<asc(str(z[0])):            
            return [lst[-1]]+z[1::]+[z[0]]
        else:
            return [lst[i^1] for i in range(len(lst[0:-1]))]+[lst[-1]]
    if len(([i for i in lst if type(i)==str]))==len(lst):
        z=[asc(i)for i in lst] 
        if z[1]>z[-1]:
            a=[lst[i^1] for i in range(len(lst[0:-1]))]+[lst[-1]]
            return [a[-1]]+a[1:-1]+[a[0]]
        if asc(lst[-1])>asc(lst[0]):
            return [lst[i^1] for i in range(len(lst[0:-1]))]+[lst[-1]]
    else:
        for i,v in enumerate(lst):  
            if type(v)==str:
                x.append([asc(str(v)),v])
            else:
                x.append([asc(str(v)),v])
        a=sorted([i for i in x])
        return [i[1]for i in a]

