
def divisibility_rule(n):
    seq, rem = [1, 10, 9, 12, 3, 4], set()
    while n not in rem:
        rem.add(n)
        n = sum(seq[i % 6] * int(c) for i, c in enumerate(str(n)[::-1]))
    return n

