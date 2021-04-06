
def collatz(n):
    seq = [n]
    while seq[-1] != 1:
        seq.append(seq[-1] * 3 + 1 if seq[-1] % 2 else seq[-1] // 2)
    return (len(seq), max(seq))

