
def junction_or_self(n):
    x=0
    abc=[]
    for a in range(1,n):
        tot = 0
        b=str(a)
        for nums in b:
            tot=int(nums)+tot
        tot=tot+a
        if tot==n:
            x=1
            abc.append(a)
    if x==1:
        abc.sort(reverse=True)
        return abc
    else:
        return 'Self'

