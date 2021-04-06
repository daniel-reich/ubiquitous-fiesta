
def check(n, f):
    for i in range(1, n):
        f+=1
        f=check(i,f)
    return f
​
def tower_hanoi(n):
    return check(n+1, 0)

