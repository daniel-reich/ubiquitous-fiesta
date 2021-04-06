
def stupid_addition(a, b):
  if type(a) != type(b):
    return None
  elif type(a) == str:
    return int(a) + int(b)
  else:
    return str(a) + str(b)

