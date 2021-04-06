
def fibo(n):
    p = 1
    b = 1
    a = []
    x = 0
    while x < n:
        a.append(p)
        temp = p
        p = b
        b = p + temp
        x += 1
    return a[-1]

