
def number_groups(a, b, c):
    a, b, c, x, y = set(a), set(b), set(c), [], []
    if a.intersection(b) or a.intersection(c) or b.intersection(c):
        y = list((a.intersection(b), a.intersection(c), b.intersection(c)))
    [[x.append(a) for a in i] for i in y]
    x = list(set(x))
    return sorted(x)

