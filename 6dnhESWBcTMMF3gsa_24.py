
def stupid_addition(a, b):
  if type(a) is int and type(b) is int:
    return str(a) + str(b)
  if type(a) is str and type(b) is str:
    return int(a) + int(b)
  else:
    return None

