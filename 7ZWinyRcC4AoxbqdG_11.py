
def fibo(n):
    a, b, c = 0, 1, 0
    if n==1:
        return 1
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return c

