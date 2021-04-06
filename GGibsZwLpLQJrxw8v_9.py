
def get_lucky_number(size, n):
    a= list(range(1,size+1))
    x=a[1]
    for i in range(1,size+1):
        del a[x-1::x]
        x=a[i]
        l=len(a)
        if i==l-1:
            break
    return a[n-1]

