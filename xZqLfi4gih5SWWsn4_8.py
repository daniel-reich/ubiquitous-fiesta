
def license_plate(src, n, dst=''):
    if src:
        src, ch  = src[:-1].strip('-'), src[-1].upper()
        if len(dst) % (n+1) == n:
            dst = '-' + dst
        return license_plate(src, n, ch + dst)
    return dst

