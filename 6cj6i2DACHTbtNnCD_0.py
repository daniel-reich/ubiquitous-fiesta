
def two_product(lst, n):
  for i in lst:
    if n/i in lst:
      return sorted([i, int(n/i)])
  return None

