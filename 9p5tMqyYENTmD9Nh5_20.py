
def is_valid_hex_code(txt):
    f = lambda t: all(c in "0123456789abcdef" for c in t.lower())
    return txt[0] == "#" and len(txt) == 7 and f(txt[1:])

