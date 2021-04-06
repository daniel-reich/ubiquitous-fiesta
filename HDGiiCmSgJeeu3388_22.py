
def choose_fuse(fuses, current):
    new = []
    for f in fuses:
        f = int(f[:-1])
        if f >= float(current[:-1]):
            new.append(f)
    return str(min(new)) + 'V'

