
def is_polydivisible(n):
  n = str(n)
​
  for i in range(1, len(n)):
    if int(n[:i + 1]) % (i+1):
      return False
​
  return True

