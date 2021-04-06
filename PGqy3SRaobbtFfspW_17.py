
#i feel dumb with the other solutions, lmao 
def simple_pair(lst, n):
    r=[]
    for i in lst:
        for j in lst:
            if i*j==n:
                r.append(j)
                r.append(i)
    if len(r)<=2:return None
    if r[0]<0 and len(r)==8:return r[-2::]
    return r[0:2][::-1]

