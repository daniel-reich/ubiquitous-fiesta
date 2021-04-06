
def generate_nonconsecutive(n):
    x, i = "0" * n, 1
    r = [x]
    while len(x) < n + 1:
        x = bin(i)[2:].zfill(n)
        if x not in r and "11" not in x:
            r.append(x)
        i += 1
    return " ".join(r[:-1])

