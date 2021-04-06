
def word_search(x,l):
    g=[]
    q=[]
    t=0
    for i in range(1,len(x)+1):
        if i%8==0:
            g.append(q+[x[i-1]])
            q=[]
        else:
            q.append(x[i-1])
    for w in l:
        w=w.upper()
        p=w[::-1]
        for r in range(len(g)):
            if w in ''.join(g[r])or p in ''.join(g[r]):
                t+=1
        for c in range(len(g[0])):
            cw = ''
            for r in range(len(g)):
                cw += g[r][c]
            if w in cw or p in cw:
                t+=1    
        f=''
        for a in range(15,-1,-1):
            for r in range(8):
                a-=1
                for c in range(8):
                    if a==c:
                        f+=g[r][c]
            if w in f or p in f:
                t+=1
            f=''
        for a in range(-8,8,1):
            for r in range(8):
                a+=1
                for c in range(8):
                    if a==c:
                        f+=g[r][c]
            if w in f or p in f:
                t+=1
            f=''
    return t>=len(l)

