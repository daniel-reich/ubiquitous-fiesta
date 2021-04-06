
def row_sum(n):
    a = int(.5*(n**2-n+2))
​
    ctr = 0
​
    for i in range(n):
        ctr += a+i
    return ctr

