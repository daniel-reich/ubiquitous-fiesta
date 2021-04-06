
def little_big(n):
    k=0
    t=100
    a=[]
    for i in range(0,n):
        if i%2==0:
            a.append(5+k)
            k+=1
        else:
            a.append(t)
            t=t*2
    return a[n-1]

