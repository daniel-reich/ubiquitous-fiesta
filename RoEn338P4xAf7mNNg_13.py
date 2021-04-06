
def shortest_path(lst):
    c='';a=1;ans=0
    le=len(lst[0])
    for i in lst:
        c+=i
    p=c.find('1')
    x=p//le
    y=p%le
    while a<int(sorted(c)[-1]):
        a+=1
        p=c.find(str(a))
        x1=p//le
        y1=p%le
        ans+=abs(x-x1)+abs(y-y1)
        x,y=x1,y1
    return ans

