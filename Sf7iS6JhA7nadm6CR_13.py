
def divisibility_rule(n):
    seq = [1, 10, 9, 12, 3, 4]
    m = sum(seq[i%6]*j for i, j in enumerate(map(int, str(n)[::-1])))
    if m == n:
        return m
    return divisibility_rule(m)

