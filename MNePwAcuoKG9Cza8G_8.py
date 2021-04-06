
def build_staircase(height, block):
    t = []
    for j in range(1, height + 1):
        b_len = block * j
        d_len = "_" * (height - j)
        t.append(list(b_len + d_len))
    return t

