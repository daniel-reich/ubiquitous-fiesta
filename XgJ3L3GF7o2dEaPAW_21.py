
def shared_letters(a, b):
    x = ",".join(a.casefold()).split(",")
    x1 = ",".join(b.casefold()).split(",")
    k = [w for w in x if w in x and w in x1]
    k1 = set(k)
    return "".join(sorted(k1))

