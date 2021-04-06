
def is_valid_hex_code(txt):
    import re
    pattern = r'^\#[0-9A-Fa-f]{6}$'
    if re.search(pattern, txt):
        return True
    else:
        return False

