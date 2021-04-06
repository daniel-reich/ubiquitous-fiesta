
def max_product(n):
    max=0
    lst=[]
    for i in range(0,n+1):
        mul=1
        k=i
        for j in range(len(str(k)),1,-1):
            m=i//(10**(j-1))
            mul*=m
            i=i-m*(10**(j-1))
        mul*=i
        if mul>max:
            lst=[]
            lst.append(k)
            max=mul
        elif mul==max:
            lst.append(k)
    return lst

