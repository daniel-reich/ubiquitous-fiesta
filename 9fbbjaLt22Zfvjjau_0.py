
def paul_cipher(txt):
    res, shift = [], 0
    for c in txt.upper():
        if c.isalpha():
            c_pos = ord(c) - 65
            new_c = chr((c_pos + shift) % 26 + 65)
            shift = c_pos + 1
        else:
            new_c = c
        res.append(new_c)
    return "".join(res)

