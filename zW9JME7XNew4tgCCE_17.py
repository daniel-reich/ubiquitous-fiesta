
def reversible_inclusive_list(s, e):
  return list(range(s, e+1)) if s<e else list(range(e, s+1))[::-1]

