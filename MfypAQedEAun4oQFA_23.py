
def perrin(n):
    a=[3,0,2]
    if n<2:
        return a[n]
    else:
        for i in range(n-2):
            a.append(a[i]+a[i+1])
    return a[-1]

