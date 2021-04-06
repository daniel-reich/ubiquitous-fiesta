
def pascals_triangle(n):
    from functools import reduce
    def cas(n):        
        return 1 if n == 0 else reduce(lambda a,b:a*b, [i for i in range(1,n+1)])
    lst1 = []
    for i in range(1,n+1):
        for k in range(i):
            lst1.append(int(cas(i-1)/(cas(k)*cas(i-k-1))))
    return lst1

