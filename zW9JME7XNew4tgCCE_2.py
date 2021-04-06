
def reversible_inclusive_list(s, e):
  return list([range(s, e+1), range(s, e-1, -1)][s > e])

