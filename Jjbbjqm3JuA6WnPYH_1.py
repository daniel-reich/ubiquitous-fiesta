
def bit_rotate(n, m, d):
    b = bin(n)[2:]
    pos = len(b) - m if d else m
    return int(b[pos:] + b[:pos], 2)

