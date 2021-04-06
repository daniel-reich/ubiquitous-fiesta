
def golomb(n):
    a = [0,1]
    for i in range(1,n):
        a.append(1+a[i+1-a[a[i]]])
    return a[1:]

