
def gcd(a,b):
    if a==0:
        return b
    else :
        return gcd(b%a,a)
def is_prim_pyth_triple(lst):
    lst.sort()
    return lst[0]**2+lst[1]**2==lst[2]**2 and gcd(lst[0],lst[1])==1

