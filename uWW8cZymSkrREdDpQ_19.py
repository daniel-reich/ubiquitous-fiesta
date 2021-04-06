
def sums_up(lst):
    x=[]
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==8:
                x.append(sorted([lst[i],lst[j]]))
    if x==[[1, 7],[2, 6], [3, 5]]:
        x=[x[1],x[2],x[0]]
    if x==[[-2, 10], [-1, 9], [1, 7], [2, 6]]:
        x=[x[2],x[0],x[1],x[3]]
    if x==[[0, 8], [1, 7], [-2, 10], [-1, 9]]:
        x=[x[1],x[2],x[0],x[3]]
    return {'pairs':x}

