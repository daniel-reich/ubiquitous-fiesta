
def combine(lst):
    d={}
    x=[]
    for i in range(len(lst)):
        a=lst[i][0]
        if a not in x:
            x.append(a)
    y=[]
    i=0
    while i<len(lst):
        y.append([lst[i][-1],lst[i+1][-1]])
        i+=2
    return dict(zip(x,y))

