
def divide(x, y, foo=None):
  if foo is None:
    return divide(x, y, True)
  return int(x / y)

