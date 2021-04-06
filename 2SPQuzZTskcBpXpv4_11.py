
def euclidean(a, b):
  while True:
    if a < b:
      tempvar = a
      a = b
      b = tempvar
    r = a % b
    if r == 0:
      return b
    else:
      a = b
      b = r

