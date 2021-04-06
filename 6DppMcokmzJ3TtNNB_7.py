
def true_alphabetic(txt):
    k = sorted(w for w in txt if w.isalpha())[::-1]
    return ''.join(k.pop() if w.isalpha() else w for w in txt)

