
def unmix(txt):
    if len(txt) < 2: return txt
    return txt[1] + txt[0] + unmix(txt[2:])

