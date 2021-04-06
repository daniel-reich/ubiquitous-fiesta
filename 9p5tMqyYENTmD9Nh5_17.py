
def is_valid_hex_code(txt):
  valid = '0123456789ABCDEFabcdef'
  return txt[0] == '#' and all(c in valid for c in txt[1:]) and len(txt) == 7

