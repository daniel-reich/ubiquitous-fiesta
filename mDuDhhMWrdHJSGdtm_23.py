
def is_exactly_three(n):
    if n<4:return False
    if n<11:
        q=n//2
    else:
        q=int(n**.5)
    k=0
    for i in range(2,q+1):
        if n%i==0:
            k+=1
            if k>1:
                return False
    if k==0:
        return False
    return True

