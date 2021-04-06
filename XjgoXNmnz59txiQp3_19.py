
def split(x):
  if x == 1:
    return 1
  if x % 3 == 0:
    return 3 ** (x / 3)
  elif x % 3 == 1:
    return 4 * 3 ** ((x - 4) / 3)
  else:
    return 2 * 3 ** ((x - 2) / 3)

