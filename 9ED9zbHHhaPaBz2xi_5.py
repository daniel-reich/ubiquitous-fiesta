
def normal_sequence(n):
  rem = n % 8
  if rem in (1, 5):
    return 0
  elif rem in (2, 3, 0):
    return 1
  return 2

