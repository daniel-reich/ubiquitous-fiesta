
def josephus(n, k):
    p = 0
    for i in range(1, n + 1):
        p += k
        p %= i
    return p+1

