
def is_polydivisible(n):
  return all(not int(str(n)[:idx+1]) % (idx + 1) for idx, _ in enumerate(str(n)))

