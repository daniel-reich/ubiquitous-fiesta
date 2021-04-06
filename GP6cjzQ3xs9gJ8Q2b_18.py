
def is_polydivisible(n):
  s = str(n)
  for i in range(1,len(s)+1):
    if int(s[:i]) % i != 0:
      return False
  return True

