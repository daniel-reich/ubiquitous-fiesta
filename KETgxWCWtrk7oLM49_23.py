
from operator import itemgetter
def tournament_scores(lst):
    d=dict.fromkeys(['A','B','C','D'],[0,0,0])
    for x in lst:
        p1=int(x[2])
        p2=int(x[6])
        a=[0,p1,p2]
        b=[0,p2,p1]
        if p1>p2:
            a[0]=3
        elif p2>p1:
            b[0]=3
        else:
            a[0]=b[0]=1
        d[x[0]]=[sum(x) for x in zip(d[x[0]],a)]
        d[x[8]]=[sum(x) for x in zip(d[x[8]],b)]
    return sorted([[x,y[0],y[1],y[1]-y[2]] for x,y in d.items()],key=itemgetter(1,2,3),reverse=True)

