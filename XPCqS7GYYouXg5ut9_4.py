
def simplify_sqrt(n):
    if n == 1:
        return 1,1
    f, sq = 2, 4
    while sq <= n:
        q, r = divmod(n, sq)
        if r == 0:
            an, bn = simplify_sqrt(q)
            return f * an, bn
        f += 1
        sq = f * f
    return 1, n

