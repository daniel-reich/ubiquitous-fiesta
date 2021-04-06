
def legendre(p, n):
    e=s=0
    k=1
    while n>=e:
        e=p**k
        s+=int(n/e)
        k+=1
    return s

