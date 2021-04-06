
def random(x):
    m=2**16-1
    mi=1
    while (x[0]*mi)%m!=1:
        mi+=1
        if mi>m-1:
            return None
    a=((x[1]-1)*mi)%m
    return (a*x[1]+1)%m

