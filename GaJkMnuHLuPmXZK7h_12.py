
def letters(w1, w2):
    shared = "".join(sorted(set([a for a in w1 if a in w2])))
    unique1 = "".join(sorted(set([a for a in w1 if not a in w2])))
    unique2 = "".join(sorted(set([b for b in w2 if not b in w1])))
    return [shared, unique1, unique2]

