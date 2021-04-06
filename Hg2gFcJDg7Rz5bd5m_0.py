
def intersection(h1, h2):
    a = {k: v for k, v in h1.items() if k in h2}
    b = {k: v for k, v in h2.items() if k in h1}
    return [a, b]

