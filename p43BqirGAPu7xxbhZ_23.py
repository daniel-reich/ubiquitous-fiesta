
def diamond(n):
    odd=False
    d=[]
    if(n%2==0):
        mid=int(n/2)
​
    else:
        mid=int(n/2)+1
        odd=True
    m=mid
    for i in range(mid):
        l=[]
        m=m-1
        for j in range(mid):
            if(j==m):
                l.append(1)
            else:
                l.append(0)
​
        if(odd):
            tmp=l[0:mid-1]
            tmp.reverse()
            l=l+tmp
        else:
            tmp=l[0:mid]
            tmp.reverse()
            l=l+tmp
        d.append(l)
    tmp=d[0:mid-1]
    tmp.reverse()
    d=d+tmp
    diams=[]
    diams.append(d)
    if(d[0].count(1)==1):
        diams.append('perfect cut')
    else:
        diams.append('good cut')
    # print(diams)
    return diams

