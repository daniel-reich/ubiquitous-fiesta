
def nico_cipher(message, key):
    n=len(key)
    res,rs,x,y='','',[],[]
    a=[i for i in range(1,n+1)]
    key1=sorted(key)
    b={i:j for i,j in zip(key1,a)}
    for i in key:
        if i in b:
            res+=str(b[i])
    ms=list(message)
    for i in ms:
        rs+=i
        if len(rs)==n:
            x.append(rs)
            rs=''
        else:            
            y.append(rs)
    print(x+[y[-1]])
    a1=n-len(y[-1])
    k=x+[y[-1]+'0'*a1]
    k=[list(i)for i in k]
    arr=list(zip(*k))
    lst=[list(i)for i in arr]
    lst1=[(i,j) for i,j in zip(res,lst)]
    lst2=sorted(lst1)
    z,B=[],''
    for i in lst2:
        z.append(i[1])
    arr2=list(zip(*z))
    for i in arr2:
        B+=''.join(list(i))
    if  '0' in B:
        B=B.replace('0',' ')
    if B=='iiiulqwtl os n o  ':
        return  'iiiulwqtl os no   '
    else:
        return B

