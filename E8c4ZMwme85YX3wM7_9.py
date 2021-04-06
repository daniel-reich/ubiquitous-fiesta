
def recaman(n):
    rs=[];k=0
    if n>0:rs=[0]
    while len(rs)<n:
        t=rs[k]-(k+1)
        if t>0 and t not in rs:
            rs.append(t)
        else:
            rs.append(rs[k]+k+1)
        k+=1
    dup=[]
    for i in range(len(rs)):
        if rs[i] in rs[:i] and rs[i] not in dup:
            dup.append(rs[i])
    r="---> Recaman's sequence: %s\n---> Duplicates for n = %s: %s" %(rs,n,dup)
    return r.format(rs,n,dup)

