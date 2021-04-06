
import math
def dartboard(i,n):
    for i in range(1,n+1):
        row='{:0^{}}'.format('1'*i,n)
    return row       
def make_dartboard(n):
    x,y,b=[],[],''
    m=math.ceil(n/2)
    for i in range(1,m+1):
        x.append(dartboard(i,n))
    y.append(x[0])
    x=x[0::]
    i=0
    while len(x)>len(y):
        a=y[i]
        i+=1
        e=a[i:-i]
        c=a[:i]
        for j in e:
            j=int(j)+1
            b+=str(j)
        z=c[::-1]   
        d=str(c)+b+str(z) 
        y.append(d)
        b=''
    if n%2==0:    
        p=y
    else:
        p=y[0:-1]
    return [int(i)for i in(y+p[::-1])]

