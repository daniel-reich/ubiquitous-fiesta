
def filter_factorials(l):
    import math
    n=l[-1]
    i=1
    a=[]
    b=1
    while b<=n:
        b=math.factorial(i)
        a.append(b)
        i+=1
    return sorted(list(set(l) & set(a)) )

