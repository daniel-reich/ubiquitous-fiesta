
def max_separator(lst):
    
    a = list(lst)
    c,d,e,f,g=[],[],[],[],[]   
    for p in range(len(a)):
        k = str("c"+str(p))
        k= []
        c.append(k)    
    for i in range(len(c)):
        c[i].append(a[i])
        for j in range(i+1,len(c)):
            c[i].append(a[j])          
            if a[j] == a[i]:
                d.append(c[i])
                break
    if len(d)==0:
        return []    
    ds = sorted(d,key=len,reverse=True)
    for i in ds:
        e.append(len(i))    
    f.append(e[0])
    for i in range(1,len(e)):
        if (e[i-1])!=(e[i]):
            break
        f.append(e[i])    
    for i in range(len(f)):
        g.append(ds[i])
    result = []
    for i in range(len(g)):
        result.append(sorted(g)[i][0])
    return result

