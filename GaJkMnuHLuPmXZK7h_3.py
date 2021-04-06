
def letters(w1, w2):
    s1, s2 = set(w1), set(w2)
    return [''.join(sorted(i)) for i in [s1&s2, s1-s2, s2-s1]]

