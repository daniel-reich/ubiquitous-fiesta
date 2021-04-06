
def snakefill(n):
    if n== 2:
        return 2
    cnt = 0
    res = 1
    for x in range(1, n+1):
        res *= 2
        cnt += 1
        if res > n * n:
            return cnt-1

