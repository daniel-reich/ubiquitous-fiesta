
def pi(n):
    md=2
    mt=100
    x=3*10**int(n*md)
    res=x
    for k in range(1,int(n*mt)):
        x*=2*k-1
        x//=2*k*4
        res+=x//(2*k+1)
    return '3.'+str(res)[1:n+1]

