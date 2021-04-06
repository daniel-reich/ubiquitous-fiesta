
def wrap_around(s, offset):
    return s[offset%len(s):] + s[:offset%len(s)]

