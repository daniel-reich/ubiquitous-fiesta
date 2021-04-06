
def recaman(n):
    seq = []
    duplicates = []
    if n > 0:
        seq.append(0)
        for idx in range(1, n):
            x = seq[-1] - idx
            if x > 0 and x not in seq:
                seq.append(x)
            else:
                seq.append(seq[-1] + idx)
    for idx, x in enumerate(seq):
        if x in seq[:idx] and x not in duplicates:
            duplicates.append(x)
    return ('---> Recaman\'s sequence: {}\n---> Duplicates for n = {}: {}'
            .format(seq, n, duplicates))

