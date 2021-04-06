
def invert(s):
    if not s:
        return s
    return invert(s[1:]) + s[0].swapcase()

