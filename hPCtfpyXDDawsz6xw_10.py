
def verbify(txt):
    t = txt.split()
    if t[0][-1] == 'e' or t[0][-1] == 'd':
        if t[0][-1] == 'e':
            t[0] += 'd'
        elif t[0][-2] != 'e':
            t[0] += 'ed'
    else:
        t[0] += 'ed'
    return ' '.join(t)

