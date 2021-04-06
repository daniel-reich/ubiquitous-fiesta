
def is_valid_phone_number(txt):
  return txt[0] == '(' and txt[4:6] == ') ' and txt[9] == '-' and len(txt) == 14

