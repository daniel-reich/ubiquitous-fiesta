
def sum_digits(a, b):
    s=0
    for i in range (a,b+1):
        l=len(str(i))
        n=i;
        for j in range(l):
            s+=n%(10)
            n=int(n/10)
    return s

