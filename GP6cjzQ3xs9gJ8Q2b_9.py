
def is_polydivisible(n):
  bias = 1
  n = str(n)
  while bias < len(n) + 1:
    if int(n[:bias])%bias != 0:
      return False
    bias += 1
  return True

