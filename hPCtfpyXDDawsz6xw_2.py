
def verbify(txt):
    if 'ed ' in txt:
        return txt
    if 'e ' in txt:
        return txt.replace('e ', 'ed ')
    return txt.replace(' ', 'ed ')

