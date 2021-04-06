
def alphanumeric_restriction(s):
  if ' ' in s or s == "":
    return False
  else:
    if s.isalpha() == True or s.isdigit() == True:
      return True
    else:
      return False

