
def valid(txt):
  if 4 != len(txt) != 6:
    return False
  if not txt.isnumeric():
    return False
  return True

