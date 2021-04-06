
def pyramidal_string(string, _type):
    if _type == 'REG':
        st = string
    elif _type == 'REV':
        st = string[::-1]
    ln = 1
    lout = []
    while len(st) >= ln:
        s2 = ' '.join(list(st[:ln]))
        st = st[ln:]
        if _type == 'REG':
            lout.insert(len(lout), s2)
        elif _type == 'REV':
            lout.insert(0, s2[::-1])
        ln += 1
        if 0 < len(st) < ln:
            return "Error!"
    return lout

