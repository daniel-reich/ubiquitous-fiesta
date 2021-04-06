
def fib_str(n, f):
    f1=f
    x=[]
    x.append(f[0])
    x.append(f[1])
    f=sorted(f)
    if f1!=f:
        a=f[0]
        b=f[1]
        f[1]=f1[1]
    print(f,f1)
    c=a+b
    d=f[1]
    n=n-3
    x.append(c)
    for _ in range(n):
        m=c+d
        x.append(m)
        d=c
        c=m        
    return ', '.join(x)

