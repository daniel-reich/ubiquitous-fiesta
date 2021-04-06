
def dice_game(scores):
    p='1234'
    while len(p)>1:
        pl=len(p)
        s=scores[:pl]
        s=[sum(s[i]) for i in range(pl)]
        t=[i for i in range(pl) if s[i]==min(s)]
        k=set([scores[i][0] for i in t])
        if len(k)==len(t):
            m=7
            for i in t:
                if scores[i][0]<m:
                    m=scores[i][0]
                    x=i
            p=p.replace(p[x],'')      
        scores=scores[pl:]      
    return 'p'+p

