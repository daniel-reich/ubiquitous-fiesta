
def is_polydivisible(n):
  n1 = str(n)
  for i in range(len(n1)):
    r = int(n1[0:i+1]) % (i+1)
    if r != 0:
      return False
  return True

