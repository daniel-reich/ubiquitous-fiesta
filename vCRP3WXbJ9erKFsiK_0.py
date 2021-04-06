
def dif_ciph(x):
    if isinstance(x, str):
        return [ord(x[0])] + [ord(b) - ord(a) for a, b in zip(x, x[1:])]
    return ''.join(chr(sum(x[:i])) for i in range(1, len(x) + 1))

