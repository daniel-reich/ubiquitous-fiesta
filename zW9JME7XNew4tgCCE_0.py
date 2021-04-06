
def reversible_inclusive_list(n, m):
  s = -1 if n > m else 1
  return list(range(n, m+s, s))

