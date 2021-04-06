
def can_put(txt, dim):
    sw = txt.split()
    ts = ' '.join(sw)
    mx = max(len(Z) for Z in sw)
    if dim[1] >= len(ts):
        return True
    else:
        if len(sw) > dim[0]:
            return False
        if mx > dim[1]:
            return False
    return True

