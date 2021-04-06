
def count_same_ends(txt):
    lst = ''.join(l.lower() for l in txt if l not in '.!')
    return sum(1 for w in lst.split() if w[0] == w[-1]  and len(w) > 1)

