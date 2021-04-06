
def partitions(n):
    def p(n, mx):
        return sum(p(n-i, min(i, n-i)) for i in range(1, mx+1)) if n else 1
    return p(n, n)

