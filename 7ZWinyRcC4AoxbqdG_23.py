
def fibo(n):
    a=1
    b=1
    j=2
    while j < n:
        c=b+a
        a=b
        b=c
        j=j+1
    return b

