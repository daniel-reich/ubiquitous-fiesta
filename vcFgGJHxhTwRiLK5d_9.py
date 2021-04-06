
def smallest(n):
    def factors(n):
        res=[]
        for i in range(2,n+1):
            while True:            
                if n%i==0:
                    res.append(i)
                    n=n//i
                else:
                    break
        return res
    factlist,prod=[],1
    for i in range(2,n+1):
        f=factlist[:]
        for elem in factors(i):            
            if elem in f:
                f.remove(elem)
            else:
                factlist.append(elem)
                prod*=elem
    return prod

