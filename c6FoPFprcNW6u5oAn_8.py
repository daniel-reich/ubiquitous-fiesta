
def farey(n):
    l = []
    for k in range(1,n):
        for j in range(k+1,n+1):
            i,x,y = k,k,j
            while y != 0:
                (x, y) = (y, x % y)
            i /= x; i = int(i); j /= x; j = int(j)
            l.append(("/".join(map(str,[i,j]))))
    return ["0/1"] + sorted(set(l),key = eval) + ["1/1"]

