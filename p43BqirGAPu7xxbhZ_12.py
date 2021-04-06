
def diamond(carat):
    res=[]
    if carat%2==1:
        edges,correct=[carat//2,carat//2],0
    else:
        edges,correct=[carat//2-1,carat//2],1
    for i in range(carat-correct):
        row=[]
        for j in range(carat):
            char=0 if j not in edges else 1
            row.append(char)
        res.append(row)
        if i <carat//2-correct:
                edges[1]+=1
                edges[0]-=1
        else:
                edges[0]+=1
                edges[1]-=1
    return [res,"perfect cut" if carat%2==1 else "good cut"]

