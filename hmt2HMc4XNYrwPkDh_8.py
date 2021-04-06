
def invert(s):
    if len(s) == 0:
        return s
    else:
        return invert(s[1:]) + s[0].swapcase()

