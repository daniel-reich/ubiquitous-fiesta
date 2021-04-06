
def is_early_bird(r, n):
    s='';ans=[];p=0
    for i in range(r+1):
        s=s+str(i)
    while p>=0:
        p=s.find(str(n),p+1)
        if p!=-1:
            ans.append([p+i for i in range(len(str(n)))])
    if len(ans)>1:
        ans.append('Early Bird!')
    return ans

