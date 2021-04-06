
def factorl(i):
    return len([x for x in range(1,i+1) if i%x==0 ])
def factor_sort(n):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if factorl(n[i]) < factorl(n[j]):
                n[i],n[j]=n[j],n[i]
            if factorl(n[i]) == factorl(n[j]):
                if n[i] < n[j]:
                    n[i],n[j]=n[j],n[i]
    return n

