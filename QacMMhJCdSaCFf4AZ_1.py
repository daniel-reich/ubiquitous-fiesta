
def sequence_generator(seq):
    # test arithmetic series:
    diffs = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    if len(set(diffs)) == 1:
        # it's a arithmetic series:
        a = diffs[0]
        c = seq[0] - a
        return lambda n: a * n + c
    else:
        # it's a geometric series:
        a = seq[1] // seq[0]
        c = seq[0]
        return lambda n: pow(a, n - 1) * c

