
def is_repeated(strn):
  if strn[0] == strn[1]:
    return 24
  if strn[0] == strn[2]:
    return 12
  if strn[0] == strn[3]:
    return 8
  if strn[0] == strn[4]:
    return 6
  if strn[0] == strn[6]:
    return 4
  if strn[0] == strn[8]:
    return 3
  if strn[0] == strn[12]:
    return 2
  return False

