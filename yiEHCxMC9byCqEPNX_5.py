
def is_palindrome(p, clean=False):
    if not clean:
        p = ''.join(c.lower() for c in p if c.isalpha())
    if len(p) == 1:
        return True
    elif len(p) == 2:
        return p[0] == p[1]
    return is_palindrome(p[1: -1], True) if p[0] == p[-1] else False

