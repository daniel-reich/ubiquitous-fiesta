
def is_valid_hex_code(txt):
  if len(txt) != 7 or txt[0] != "#":
    return False
  txt = txt.upper()
  for letter in txt:
    if not letter in "#123456789ABCDEF":
      return False
  return True

