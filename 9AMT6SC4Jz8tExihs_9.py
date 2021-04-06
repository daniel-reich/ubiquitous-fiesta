
def countStrings(n):
    x=[]
    x.append(0)
    p = (1 << n)
    for i in range(1, p):
        if ((i & (i << 1)) == 0):
            x.append(i)
    return x        
def generate_nonconsecutive(n):
    res,c='',n
    for i in countStrings(n):
        a=bin(i).replace('b','')
        if len(a)<c:
            b='0'*(c-len(a))
            a=b+a
        d=len(a)-c
        res+=a[d:]+' '
    return res.strip()

