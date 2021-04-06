
def check_pattern(lst, p):
    t='ABCD'
    for i in t:
        d=[]
        e=[0,1,2,3]
        n=p.count(i)
        k=0
        for j in range(n):
            m=p.find(i,k)
            d.append(m)
            e.remove(m)
            k=m+1
        if len(d)>1:
            for j in range(len(d)-1):
                if lst[d[j]]!=lst[d[j+1]]:
                    return False
                for f in e:
                    if lst[d[j]]==lst[f]:
                        return False
    return True

