
def is_valid_hex_code(txt):
    hexst = '#0123456789ABCDEF'
    return len(txt) == 7 and ''.join(h for h in txt if h.upper() in hexst).upper() == txt.upper()

