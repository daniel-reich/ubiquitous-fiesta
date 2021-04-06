
def convert_to_hex(txt):
    return ' '.join([hex(ord(t))[2:] for t in txt])

