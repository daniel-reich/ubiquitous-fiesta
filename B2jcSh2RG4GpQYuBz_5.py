
def is_valid_phone_number(txt):
  check = True
  if txt[0] != '(':
    return False
  elif txt[4:6] != ') ':
    return False
  elif txt[9] != '-':
    return False
  elif len(txt) != 14:
    return False
  else:
    return True

