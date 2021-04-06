
def chunk(l, n):
    return [l[i-n:i] for i in range(n, len(l) + n, n)]

