
def josephus(n):
    p = 1
    for i in range(1, n + 1):
        p = (p + 2)%i
    return p + 1

