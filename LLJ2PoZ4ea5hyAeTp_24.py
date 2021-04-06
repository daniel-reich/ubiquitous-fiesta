
def DECIMATOR(txt):
    a=len(txt)
    b=a//10
    c=a/10
    if c>b:
        b+=1
    l=[]
    for i in txt:
        l.append(i)
    count=0
    a=len(l)-b
    c=[]
    for i in range(0,a,1):
        c.append(l[i])
    n=''.join(str(e) for e in c )
    return n
r=DECIMATOR("1234567890AB")
print(r)

