
def unrepeated(txt):
    new = []
    for c in txt:
        if c not in new:
            new.append(c)
    return ''.join(new)

