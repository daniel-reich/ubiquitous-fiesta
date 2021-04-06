
def fact_of_fact(n):
    if n == 1:
        return 1
    f = [1]
    a = 0
    for i in range(2,n+1):
        f.append(i*f[a])
        a += 1
    myans = 1
    for i in f:
        myans *= i
    return myans

