
def number_groups(group1, group2, group3):
    z=[]
    h=[]
    a=set(group1)
    b=set(group2)
    c=set(group3)
    p=a.intersection(b)
    
    k=a.intersection(c)
    l=b.intersection(c)
    print(p,k,l)
    if p==set() and k==set():
        return  sorted(list(l))
    elif p==set() and l==set():
        return sorted(list(k))
    elif k==set() and l==set():
        return sorted(list(p))
​
   
    elif k==set():
        d=list(l)
        
        g=list(p)
        for u in d:
            g.append(u)
        g=list(set(g))
       
        return  sorted(g)
    elif p==set():
        d=list(l)
        
        g=list(k)
        for r in d:
            g.append(r)
        g=list(set(g))
     
        return sorted(g)
    elif l==set():
        d=list(p)
        
        g=list(k)
        for e in d:
            g.append(e)
        g=list(set(g))
        return sorted(g)
    elif ((p!=set() and k!=set()) and (l!=set())):
        x=list(p)
        y=list(k)
        z=list(l)
        for i in y:
            x.append(i)
        for j in z:
            x.append(j)
        x=list(set(x))
        return sorted(x)
    else:
        return []

