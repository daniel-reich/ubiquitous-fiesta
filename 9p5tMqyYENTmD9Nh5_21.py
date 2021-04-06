
def is_valid_hex_code(txt):
    return (txt[0] == '#' and len(txt) == 7
            and all(c.upper() in '0123456789ABCDEF' for c in txt[1:]))

