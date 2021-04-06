
def golomb(n):
    a=[1,2,2]
    if n <= 3:
        return a[:n]
    idx=[1,2]
    i=3
    while n >= len(a):
        for j in range(a[i-1]):
            a.append(i)
        i+=1
    return a[:n]

