
def mod(m, n):
    return mod(m + n, n) if m < 0 else m if m < n else mod(m - n, n)

