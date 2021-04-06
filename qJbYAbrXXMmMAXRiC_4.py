
def variable_valid(var):
  var = var.lower()
  if not 'a' <= var[0] <= 'z':
    return False
  return all([c.isalnum() or c == '_' for c in var])

