
def wrap_around(s, offset):
    if offset >= 0:
        start = offset % len(s)
        return s[start:] + s[:start]
    start = -offset % len(s)
    return s[len(s) - start:] + s[:len(s) - start]

