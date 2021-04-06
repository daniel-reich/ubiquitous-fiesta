
def true_alphabetic(txt):
    l = sorted(txt.replace(' ', ''))[::-1]
    return ''.join(l.pop() if c.isalpha() else ' ' for c in txt)

