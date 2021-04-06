
def stupid_addition(a, b):
  return None if type(a) != type(b) else str(a) + str(b) if type(a) == int else int(a) + int(b)

