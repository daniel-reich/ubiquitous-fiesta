
def is_valid_hex_code(txt):
  if len(txt) != 7:
    return False
  if txt[0] != '#':
    return False
  if len(set(txt[1:]).difference('0123456789ABCDEFabcdef')) > 0:
    return False
  
  return True

