
def invert(s, res=''):
    return invert(s[1:], s[0].swapcase() + res) if s else res

