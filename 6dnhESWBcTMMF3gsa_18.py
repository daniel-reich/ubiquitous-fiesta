
def stupid_addition(a, b):
  if isinstance(a, str) and isinstance(b, str):
    return int(a) + int(b)
  elif isinstance(a, int) and isinstance(b, int):
    return str (a) + str (b)

