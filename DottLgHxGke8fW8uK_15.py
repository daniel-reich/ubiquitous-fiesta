
def nCr(n, r):
    x = 1
    y = 1
    for i in range(min(r,n-r)):
        x *= n - i
    for j in range(1,min(r,n-r)+1):
        y *= j
    return int(x/y)
​
def nPr(n, r):
    x = 1
    for i in range(r):
        x *= n - i
    return x

