
def bar_chart(results): 
    result=results
    a,b,c,d=sorted([v for k, v in sorted(results.items())],reverse=True)
    f=sorted([k for k,v in results.items()])
    a=(int(a/50),a)
    b=(int(b/50),b)
    c=(int(c/50),c)
    d=(int(d/50),d)
    print([a,b,c,d])
    m=[a,b,c,d]
    z,e,p,l=[],[],'',[]
    for i in m:
        i=list(i)
        z.append('#'*i[0]+' '+str(i[1]))
        for k,v in sorted(results.items()):
            if i[1]==v and k not in e:
                 e.append(k)   
    for i in z:
        l.append(i.strip())
    x=[j+'|'+i for i,j in zip(l,e)]
    return '\n'.join(x)

