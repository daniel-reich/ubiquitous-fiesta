
def nico_cipher(msg, k):
    len_k, m = len(k), [[c] for c in k]
    for i, c in enumerate(msg):
        m[i % len_k].append(c)
    len_m0 = len(m[0])
    for r, row in enumerate(m):
        m[r] += [" "] * (len_m0 - len(row))
    sorted_m = [s_row[1:] for s_row in sorted(m, key=lambda rw: rw[0])]
    return "".join("".join(tpl) for tpl in zip(*sorted_m))

