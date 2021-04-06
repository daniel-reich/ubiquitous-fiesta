
def reversible_inclusive_list(s, e):
  return list(range(s, e+1)) or list(range(s, e-1, -1))

