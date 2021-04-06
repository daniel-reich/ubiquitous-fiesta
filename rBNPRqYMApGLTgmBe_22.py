
def combinations(k, n):
    a = factorial(n) / (factorial(k) * factorial(n-k))
    return a
​
def factorial(x):
    c = 1
    for i in range(x,0,-1):
        c = i*c
    return c

