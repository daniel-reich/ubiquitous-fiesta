
def legendre(p, n):
    [i,s,c] = [1,0,p]
    while(n>=c):
        s +=n//(p**i)
        i+=1
        c=p**i
    return s

