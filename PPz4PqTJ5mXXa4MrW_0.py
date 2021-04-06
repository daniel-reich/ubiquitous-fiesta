
def ulam(size):
    seq, n = {1, 2}, 3
    while len(seq) < size:
        pairs = {(i, n-i) for i in seq if n-i in seq and i < n-i}
        if len(pairs) == 1:
            seq.add(n)
        n += 1
    return max(seq)

