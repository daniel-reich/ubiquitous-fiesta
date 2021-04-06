
def alphanumeric_restriction(s):
  if s.isalpha():
    return True
  if s.isnumeric():
    return True
  else:
    return False

