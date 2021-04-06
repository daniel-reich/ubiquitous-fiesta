
def fibo(n):
    l, ll = 1, 1
    for _ in range(1, n):
        new = l + ll 
        l, ll = ll, new
    return l

