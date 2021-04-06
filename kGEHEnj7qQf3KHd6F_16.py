
def alphanumeric_restriction(s):
  if s.isdigit():
    return True
  elif s.isalpha():
    return True
  else:
    return False

