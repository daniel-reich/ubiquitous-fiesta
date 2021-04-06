
def reversible_inclusive_list(s, e):
  if s < e:
    return list(range(s,e+1))
  return list(range(s,e-1,-1))

