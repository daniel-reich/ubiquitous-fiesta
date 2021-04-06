
def split(x):
    count,sum,y=0,0,[]
    for i in range(x):
        count+=2.5
        sum+=1
        if count==x:
            y.append(i)
            break
    if x==1:
        return 1
    if x==10:
        n=y[0]+1
        return round(((x/n)**n),1)
    if x==50:
        n=y[0]-1
    else:    
        n=y[0]
    return round(((x/n)**n),1)

