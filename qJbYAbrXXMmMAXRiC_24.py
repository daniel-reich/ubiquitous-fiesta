
def variable_valid(var):
  if var[0].isnumeric() or " " in var:
    return False
  else:
    return True

