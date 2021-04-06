
def stupid_addition(a, b):
  if type(a) != type(b):
    return None
  if type(a) == str:
    return int(a) + int(b)
  else:
    return str(a) + str(b)

