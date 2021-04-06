
def diamond(x):
    v=[]
    for a in range(0,x):
        v.append(0)
    a=0
    b=x-1
    v[0]=1
    v[x-1]=1
    f=[v]
    if x%2==0:
        while abs(a-b)>1:
            g=[]
            for u in range(0,x):
                g.append(0)
            a=a+1
            b=b-1
            g[a]=1
            g[b]=1
            f.append(g)
            f.insert(0,g)
            w='good cut'
    else:
        while abs(a-b)>2:
            g=[]
            for u in range(0,x):
                g.append(0)
            a=a+1
            b=b-1
            g[a]=1
            g[b]=1
            f.append(g)
            f.insert(0,g)
        z=int((x-1)/2)
        t=[]
        for a in range(0,x):
            t.append(0) 
        t[z]=1
        f.append(t)
        f.insert(0,t)
        w='perfect cut'
    final=[]
    final.append(f)
    final.append(w)
    return final

