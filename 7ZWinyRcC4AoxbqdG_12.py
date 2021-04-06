
def fibo(n):
    if n == 1 or n == 2:
        return 1
    last = 1
    lastlast = 1
    val = 0
    for _ in range(2, n):
        val = last + lastlast
        lastlast = last
        last = val
    return val

