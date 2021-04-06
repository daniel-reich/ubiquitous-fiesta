
def neighboring(txt):
    return all(abs(ord(a) - ord(b)) == 1 for a, b in zip(txt, txt[1:]))

