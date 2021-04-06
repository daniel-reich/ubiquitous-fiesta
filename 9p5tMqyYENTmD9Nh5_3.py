
def is_valid_hex_code(txt):
    import re
    return bool(re.match(r'#[0-9A-Fa-f]{6}\b', txt))

