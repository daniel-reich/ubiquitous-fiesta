
def variable_valid(var):
  print(var)
  if var[0].isalpha() and " " not in var:
    return True
  else:
    return False

