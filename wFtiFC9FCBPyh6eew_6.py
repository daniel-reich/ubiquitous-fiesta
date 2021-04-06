
def partitions(n):
    if n in (0, 1):
        return 1
    elif n<0:
        return 0
    else:
        k = 1
        p = 0
        while (k*(3*k-1)<=2*n):
            p = p + ((-1)**(k+1)) * (partitions(n-k*(3*k-1)/2) + partitions(n-k*(3*k+1)/2))
            k = k+1
    return p

