
def f(A,c):
    d=c**2-16*A**2/(c**2)
    if d<0:
        return "Does not exist"
    x1=0.5*(c+d**0.5)
    x2=0.5*(c-d**0.5)
    if x1>0 and x1<c:
        x=x1
    elif x2>0 and x2<c:
        x=x2
    else: 
        return "Does not exist"
    l1=(x**2+(2*A/c)**2)**0.5
    l2=((c-x)**2+(2*A/c)**2)**0.5
    if -1*int(l1*1000)*10+int(l1*10000)>=5:
        l1=float(int(l1*1000)+1)/1000
    else:
        l1=float(int(l1*1000))/1000
    if -1*int(l2*1000)*10+int(l2*10000)>=5:
        l2=float(int(l2*1000)+1)/1000
    else:
        l2=float(int(l2*1000))/1000
    a=[l1,l2]
    if l1>l2:
        a.reverse()
    return a

